from django.db.models.signals import pre_save
from django.dispatch import receiver
from accounting.models import Transaction
import datetime

@receiver(pre_save, sender=Transaction)
def transaction_pre_save(sender, instance, **kwargs):
    if instance._state.adding:
        #print('create')
        #print(instance, instance.Bkdate[:4], instance.Bkdate[5:7])
        if instance.item.code == 0 and instance.Bkdivision == 0:
            index = 0
        else:
            if type(instance.Bkdate) == datetime.datetime:
                try:
                    index = Transaction.objects.filter(business = instance.business, item__paragraph__subsection__type = instance.item.paragraph.subsection.type, Bkdate__year = instance.Bkdate.year, Bkdate__month = instance.Bkdate.month).order_by('-proofnum').first().proofnum + 1
                except:
                    index = 1
            else:
                try:
                    index = Transaction.objects.filter(business = instance.business, item__paragraph__subsection__type = instance.item.paragraph.subsection.type, Bkdate__year = instance.Bkdate[:4], Bkdate__month = instance.Bkdate[5:7]).order_by('-proofnum').first().proofnum + 1
                except:
                    index = 1
        instance.proofnum = index
        instance.save
