from .models import Subsection, Paragraph, Item, Subdivision
from .models import Transaction, Budget
from django.db.models import Sum, Q, Case, When
from django.db.models.functions import Coalesce
import datetime

def session_info(selected_year, selected_month, session_month):
    next_year = str(int(selected_year)+1)
    selected_start_date = datetime.datetime.strptime(selected_year+"-"+session_month+"-01", "%Y-%m-%d")
    selected_end_date = datetime.datetime.strptime(next_year+"-"+session_month+"-01", "%Y-%m-%d")
    selected_date = datetime.datetime.strptime(selected_year+"-"+selected_month+"-01", "%Y-%m-%d")

    if selected_start_date <= selected_date and selected_date < selected_end_date:
        session_year = selected_year
    else:
        session_year = str(int(selected_year)-1)

    start_date = datetime.datetime.strptime(session_year+"-"+session_month+"-01", "%Y-%m-%d")
    end_date = datetime.datetime.strptime(str(int(session_year)+1)+"-"+session_month+"-01", "%Y-%m-%d")

    return {'start_date': start_date,
            'end_date' : end_date,
            'selected_date': selected_date,
            'year': session_year}

def item_info(year, btype, iotype):
    if iotype == 'i':
        return Item.objects.filter(paragraph__subsection__year = year, paragraph__subsection__institution = btype, paragraph__subsection__type = "수입").exclude(code=0)
    elif iotype == 'o':
        return Item.objects.filter(paragraph__subsection__year = year, paragraph__subsection__institution = btype, paragraph__subsection__type = "지출").exclude(code=0)
    elif iotype == 'b': #both
        return Item.objects.filter(paragraph__subsection__year = year, paragraph__subsection__institution = btype).exclude(code=0)
    else:
        return None

def subsection_info(year, btype, iotype):
    if iotype == 'i':
        return Subsection.objects.filter(year=year, institution=btype, type="수입").exclude(code=0)
    elif iotype == 'o':
        return Subsection.objects.filter(year=year, institution=btype, type="지출").exclude(code=0)
    elif iotype == 'b': #both
        return Subsection.objects.filter(year=year, institution=btype).exclude(code=0)
    else:
        return None

# 최근예산 타입 가져오기
# 본예산만 등록된 경우 본예산, 추경예산 등록된 경우 가장 높은 버전의 추경예산
def getLatestBudgetType(business, year, budget_type):
    latestBudget = Budget.objects.filter(
        business=business, year=year, type__icontains=budget_type)
    if latestBudget:
        # 본예산(type : 'revenue', 'expenditure')
        # 추경예산(type : 본예산 type 앞에 'supplementary_'가 붙음)
        # type을 오름차순으로 정렬 후 마지막꺼 가져오면 됨
        return latestBudget.order_by('type').last().type
    else:
        return ""


#=============== 예산 관련 ===============#
# 예산 관별 금액(예산)
def getBudgetSumBySubsection(business, year, subsection, budget_type):
    return Budget.objects.filter(
        business=business, year=year, item__paragraph__subsection=subsection, type=budget_type
    ).aggregate(sum=Coalesce(Sum('price'), 0))['sum']


#=============== 결산 관련 ===============#
# 거래내역 관별 기간합(결산)
# subsection 은 코드가 아닌 subsection 객체
def getTransactionSumBySubsection(business, subsection, start_date, end_date):
    if subsection.type == '수입':
        column = 'Bkinput'
    elif subsection.type == '지출':
        column = 'Bkoutput'
    return Transaction.objects.filter(
        business = business, item__paragraph__subsection = subsection.pk,
        Bkdate__gte = start_date, Bkdate__lt = end_date,
    ).aggregate(sum=Coalesce(Sum(column),0))['sum']

# 거래내역 목별 기간합(결산)
# item 은 코드가 아닌 item 객체
def getTransactionSumByItem(business, item, start_date, end_date):
    if item.paragraph.subsection.type == '수입':
        column = 'Bkinput'
    elif item.paragraph.subsection.type == '지출':
        column = 'Bkoutput'
    return Transaction.objects.filter(
        business = business, item = item.pk,
        Bkdate__gte = start_date, Bkdate__lt = end_date,
    ).aggregate(sum=Coalesce(Sum(column),0))['sum']

# 관항목 명칭별 거래내역 합 구하기
# matchYN 은 완벽일치여부: Y일 경우만 완벽일치. 나머지 경우는 포함으로 조회
# type 은 수입/지출 구분: 수입/지출 외 다른 값은 수입/지출 둘 다 포함
def getTransactionSumByName(business, type, start_date, end_date, context, matchYN):
    settlement = Transaction.objects.filter(
        business = business, Bkdate__gte = start_date, Bkdate__lt = end_date)
    if type == '수입' or type == '지출':
        settlement.filter(item__paragraph__subsection__type = type)
    if matchYN == 'Y':
        settlement = settlement.filter(
            Q(item__context=context)
            | Q(item__paragraph__context=context)
            | Q(item__paragraph__subsection__context=context)
        )
    else:
        settlement = settlement.filter(
            Q(item__context__contains=context)
            | Q(item__paragraph__context__contains=context)
            | Q(item__paragraph__subsection__context__contains=context)
        )

    return settlement.aggregate(
        sum = Coalesce(Sum(Case(
            When(Bkinput__gt = 0, then = 'Bkinput'), default = 'Bkoutput')), 0))['sum']