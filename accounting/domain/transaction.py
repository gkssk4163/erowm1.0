import datetime

from dateutil.relativedelta import relativedelta

from accounting.common import session_info
from accounting.models import Account, Transaction, TBLBANK, Deadline
from accounting.models import Item


class DeadlineCompletionError(Exception):
    def __str__(self):
        return '해당 월은 마감완료되었습니다.'


class NoTransactionHistoryForPreviousMonth(Exception):
    def __str__(self):
        return '주계좌의 전월 거래내역이 없습니다. 전월이월금을 등록해주세요.'


def registTransaction(business, transaction):
    now = datetime.datetime.now()
    start_date = datetime.datetime.strptime(transaction.Bkdate.strftime("%Y-%m-01"), "%Y-%m-%d")

    sessionInfo = session_info(str(transaction.Bkdate.year), str(transaction.Bkdate.month), business.session_month)

    a_month_ago = start_date - relativedelta(months=1)
    a_month_later = start_date + relativedelta(months=1)

    ### 전월이월금 항목 등록여부 확인
    try:
        carryover_tr = Transaction.objects.filter(business=business, Bkdate=start_date).get(Bkdivision=0)
    # 등록이 안되어 있으면 이월금 확인 및 전월이월금 항목 등록
    except Transaction.DoesNotExist:
        main_acct = Account.objects.get(business=business, main=True)
        # 주계좌 전월 마지막거래
        last_tr = TBLBANK.objects.filter(Bkacctno=main_acct.account_number, Bkdivision=1, Bkdate__gte=a_month_ago,
                                         Bkdate__lt=start_date).order_by('Bkdate', 'Bkid').last()
        # 주계좌 당월 첫거래
        first_tr = TBLBANK.objects.filter(Bkacctno=main_acct.account_number, Bkdivision=1, Bkdate__gte=start_date,
                                          Bkdate__lt=a_month_later).order_by('Bkdate', 'Bkid').first()

        # 회기 첫월이면 전월이월금 0으로 설정
        if transaction.Bkdate.month == int(business.session_month):
            carryover_Bkjango = 0
        else:
            # 전월이월금 없는 경우 주계좌 전월 마지막거래 잔액을 전월이월금으로 등록
            if last_tr != None:
                carryover_Bkjango = last_tr.Bkjango
            else:  # 주계좌 전월 마지막거래 잔액가 없는 경우
                # if first_tr.Bkjango == 0:  # 주계좌 당월 첫거래가 0이면 (처음개설계좌)
                #     carryover_Bkjango = 0  # 전월이월금 0으로 설정
                # else:
                raise NoTransactionHistoryForPreviousMonth()

        Transaction.objects.create(
            Bkid=last_tr.Bkid,
            Bkdivision=0,
            Mid=transaction.Mid,
            business=business,
            Bkacctno=main_acct.account_number,
            Bkname=main_acct.bank.name,
            Bkdate=start_date,
            Bkjukyo="전월이월금",
            Bkinput=carryover_Bkjango,
            Bkoutput=0,
            Bkjango=carryover_Bkjango,
            item=Item.objects.get(
                paragraph__subsection__year=sessionInfo['year'],
                paragraph__subsection__institution=business.type3,
                paragraph__subsection__code=0, paragraph__code=0, code=0),
            regdatetime=now
        )
    ### 전월이월금 항목 등록여부 확인 END

    ### 마감등록 확인
    try:
        close = Deadline.objects.get(business=business, year=transaction.Bkdate.year, month=transaction.Bkdate.month)
        if close.regdatetime:
            raise DeadlineCompletionError()
    except Deadline.DoesNotExist:
        pass
    ### 마감등록 확인 END

    ### 거래등록
    Bkdivision = Transaction.objects.filter(Bkid=transaction.Bkid).filter(Bkdivision__gt=0).count() + 1
    latest_tr = Transaction.objects.filter(business=business, Bkdate__lte=transaction.Bkdate) \
        .order_by('-Bkdate', '-id').first()
    jango = latest_tr.Bkjango
    Bkjango = 0
    if transaction.Bkinput > 0:
        Bkjango = jango + transaction.Bkinput
    if transaction.Bkoutput > 0:
        Bkjango = jango - transaction.Bkoutput

    tr = Transaction(
        Bkid=transaction.Bkid,
        Bkdivision=Bkdivision,
        Mid=transaction.Mid,
        business=transaction.business,
        Bkacctno=transaction.Bkacctno,
        Bkname=transaction.Bkname,
        Bkdate=transaction.Bkdate,
        Bkjukyo=transaction.Bkjukyo,
        Bkinput=transaction.Bkinput,
        Bkoutput=transaction.Bkoutput,
        Bkjango=Bkjango,
        regdatetime=now,
        item=transaction.item,
        subdivision=transaction.subdivision,
        relative_subsection=transaction.relative_subsection,
        relative_item=transaction.relative_item
    )
    tr.save()
    ### 거래등록 END

    ### TBLBANK 테이블 거래내역 동기화
    tblbank = TBLBANK.objects.get(Bkid=transaction.Bkid)
    tblbank.sub_Bkjukyo = transaction.Bkjukyo
    tblbank.item = transaction.item
    tblbank.subdivision = transaction.subdivision
    tblbank.relative_subsection = transaction.relative_subsection
    tblbank.relative_item = transaction.relative_item
    tblbank.regdatetime = now
    tblbank.save()
    ### TBLBANK 테이블 거래내역 동기화 END

    ### 잔액 업데이트
    update_list = Transaction.objects.filter(business=business, Bkdate__gt=transaction.Bkdate, Bkdate__lt=a_month_later)
    for update in update_list:
        if transaction.Bkinput > 0:
            update.Bkjango = update.Bkjango + transaction.Bkinput
        elif transaction.Bkoutput > 0:
            update.Bkjango = update.Bkjango - transaction.Bkoutput
        update.save()
    ### 잔액 업데이트 END
