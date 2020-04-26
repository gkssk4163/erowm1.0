from .models import Setting, Business, TBLBANK
from django.db import connections
from django.utils import timezone

def cron_database_syn():
    try:
        tr_num = Setting.objects.get(name="transaction_num")

        query = """SELECT * FROM TBLBANK WHERE Bkid > """+str(tr_num.value)

        with connections['default'].cursor() as cursor:
            cursor.execute(query)
            columns = [ col[0] for col in cursor.description ]
            data_list = [ dict(zip(columns,row)) for row in cursor.fetchall() ]

        try:
            num = TBLBANK.objects.all().order_by('-Bkid').first().Bkid + 1
        except:
            num = 1

        for data in data_list:
            try:
                business = Business.objects.get(account__account_number=data['Bkacctno'])
                TBLBANK.objects.create(
                    Bkid=num,
                    Bkdivision=1,
                    Mid=data['Mid'],
                    Bkacctno=data['Bkacctno'],
                    Bkname=data['Bkname'],
                    Bkdate=data['Bkdate'][:4]+'-'+data['Bkdate'][4:6]+'-'+data['Bkdate'][6:],
                    Bkjukyo=data['Bkjukyo'],
                    Bkinput=data['Bkinput'],
                    Bkoutput=data['Bkoutput'],
                    Bkjango=data['Bkjango'],
                    business=business
                )
                tr_num.value = data['Bkid']
                tr_num.save()
                num += 1
            except:
                print(str(timezone.now())+" "+ex)

        print(str(timezone.now())+" cron complete")
    except Exception as ex:
        print("--"+str(timezone.now())+" "+ex)
    return redirect('other_settings')
