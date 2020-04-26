from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Level(models.Model):
    level = models.PositiveSmallIntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    name = models.CharField(max_length=10)
    ko_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

ROLE_DEFAULT_LEVEL = 2
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.SET_DEFAULT, default=ROLE_DEFAULT_LEVEL)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''

class Bank(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Agency(models.Model):
    profile = models.OneToOneField('accounting.Profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    reg_number = models.CharField(max_length=12)
    owner_name = models.CharField(max_length=10)
    reg_date = models.DateField(default=date.today)
    owner_reg_number1 = models.CharField(max_length=6)
    owner_reg_number2 = models.CharField(max_length=45)
    cellphone = models.CharField(max_length=13)
    phone = models.CharField(max_length=13, null=True, blank=True)
    fax = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField()
    zip_number = models.CharField(max_length=5)
    address = models.CharField(max_length=45)
    detailed_address = models.CharField(max_length=20)
    bank = models.ForeignKey('accounting.Bank', on_delete=models.SET_NULL, null=True)
    account_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        sales = Sales.objects.filter(agency=self)
        if sales:
            for s in sales:
                s.delete()
        self.profile.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


class Sales(models.Model):
    profile = models.OneToOneField('accounting.Profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    jdate = models.DateField(default=date.today)
    reg_number1 = models.CharField(max_length=6)
    reg_number2 = models.CharField(max_length=45)
    cellphone = models.CharField(max_length=13)
    zip_number = models.CharField(max_length=5)
    address = models.CharField(max_length=45)
    detailed_address = models.CharField(max_length=20)
    email = models.EmailField()
    agency = models.ForeignKey('accounting.Agency', on_delete=models.SET_NULL, null=True)
    bank = models.ForeignKey('accounting.Bank', on_delete=models.SET_NULL, null=True)
    account_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.profile.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


class Owner(models.Model):
    profile = models.OneToOneField('accounting.Profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=13, null=True, blank=True)
    cellphone = models.CharField(max_length=13)
    place_name = models.CharField(max_length=15)
    reg_number = models.CharField(max_length=12)
    owner_reg_number1 = models.CharField(max_length=6)
    owner_reg_number2 = models.CharField(max_length=45)
    type1 = models.CharField(max_length=10)
    type2 = models.CharField(max_length=10)
    fax = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField()
    zip_number = models.CharField(max_length=5)
    address = models.CharField(max_length=45)
    detailed_address = models.CharField(max_length=20)
    is_demo = models.BooleanField(default=True)
    sales = models.ForeignKey('accounting.Sales', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.profile.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


class Business_type(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name


class Business(models.Model):
    owner = models.ForeignKey('accounting.Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    place_name = models.CharField(max_length=15)
    reg_number = models.CharField(max_length=12)
    owner_name = models.CharField(max_length=10)
    owner_reg_number1 = models.CharField(max_length=6)
    owner_reg_number2 = models.CharField(max_length=45)
    type1 = models.CharField(max_length=10)
    type2 = models.CharField(max_length=10)
    type3 = models.ForeignKey('accounting.Business_type', on_delete=models.PROTECT)
    cellphone = models.CharField(max_length=13)
    phone = models.CharField(max_length=13, null=True, blank=True)
    fax = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField()
    zip_number = models.CharField(max_length=5)
    address = models.CharField(max_length=45)
    detailed_address = models.CharField(max_length=20)
    s_auth_key = models.CharField(max_length=32, null=True, blank=True)
    session_month = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Account(models.Model):
    class Meta:
        unique_together = (('business', 'account_number'),)
        
    business = models.ForeignKey('accounting.Business', on_delete=models.CASCADE)
    renames = models.CharField(max_length=20)
    bank = models.ForeignKey('accounting.Bank', on_delete=models.PROTECT)
    main = models.BooleanField(default=True)
    account_number = models.CharField(max_length=64)
    account_pw = models.CharField(max_length=20)
    bkdiv = models.CharField(max_length=1)
    Mjumin_1 = models.CharField(max_length=6, null=True, blank=True)
    webid = models.CharField(max_length=30, null=True, blank=True)
    webpw = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return self.renames


class Subsection(models.Model):
    class Meta:
        unique_together = (('year', 'institution', 'type', 'code'),)
    
    year = models.CharField(max_length=4)
    institution = models.ForeignKey('accounting.Business_type', on_delete=models.PROTECT)
    type = models.CharField(max_length=2)
    code = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(11)])
    context = models.CharField(max_length=20)
    enable = models.CharField(max_length=1)

    def __str__(self):
        return "%s-[%s]%s(%s)" % (self.institution, self.type, self.context, self.code)


class Paragraph(models.Model):
    class Meta:
        unique_together = (('subsection', 'code'),)

    year = models.CharField(max_length=4)
    subsection = models.ForeignKey('accounting.Subsection', on_delete=models.PROTECT)
    code = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    context = models.CharField(max_length=20)
    enable = models.CharField(max_length=1)

    def __str__(self):
        return "%s-[%s]%s(%s%s)" % (self.subsection.institution, self.subsection.type, self.context, self.subsection.code, self.code)


class Item(models.Model):
    class Meta:
        unique_together = (('paragraph', 'code'),)

    year = models.CharField(max_length=4)
    paragraph = models.ForeignKey('accounting.Paragraph', on_delete=models.PROTECT)
    code = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    context = models.CharField(max_length=20)
    text = models.TextField()
    enable = models.CharField(max_length=1)

    def __str__(self):
        return "[%s]%s(%s%s%s)" % (self.paragraph.subsection.type, self.context, self.paragraph.subsection.code, self.paragraph.code, self.code)


class Subdivision(models.Model):
    class Meta:
        unique_together = (('item', 'code'),)

    business = models.ForeignKey('accounting.Business', on_delete=models.CASCADE)
    item = models.ForeignKey('accounting.Item', on_delete=models.PROTECT)
    code = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    context = models.CharField(max_length=20)

    def __str__(self):
        return "[%s]%s(%s%s%s%s)" % (self.item.paragraph.subsection.type, self.context, self.item.paragraph.subsection.code, self.item.paragraph.code, self.item.code, self.code)


class TBLBANK(models.Model):
    class Meta:
        unique_together = (('Bkid', 'Bkdivision'),)

    business = models.ForeignKey('accounting.Business', on_delete=models.CASCADE)
    Bkid = models.IntegerField()
    Bkdivision = models.IntegerField()
    direct = models.BooleanField(default=False)
    Mid = models.CharField(max_length=50)
    Bkacctno = models.CharField(max_length=64, null=True, blank=True)
    Bkname = models.CharField(max_length=32, null=True, blank=True)
    Bkdate = models.DateTimeField()
    Bkjukyo = models.CharField(max_length=60)
    sub_Bkjukyo = models.CharField(max_length=60, null=True, blank=True)
    Bkinput = models.BigIntegerField(null=True, blank=True)
    Bkoutput = models.BigIntegerField(null=True, blank=True)
    Bkjango = models.BigIntegerField(null=True, blank=True)
    regdatetime = models.DateTimeField(null=True, blank=True)
    item = models.ForeignKey('accounting.Item', on_delete = models.PROTECT, null=True, blank=True)
    subdivision = models.ForeignKey('accounting.Subdivision',on_delete = models.PROTECT, null=True, blank=True)
    relative_subsection = models.ForeignKey('accounting.Subsection', on_delete = models.PROTECT, null=True, blank=True)
    relative_item = models.ForeignKey('accounting.Item', on_delete = models.PROTECT, related_name="related_item", null=True, blank=True)

    def __str__(self):
        return str(self.Bkid)


class Transaction(models.Model):
    class Meta:
        unique_together = (('Bkid', 'Bkdivision'),)

    proofnum = models.IntegerField()
    Bkid = models.IntegerField()
    Bkdivision = models.IntegerField()
    Mid = models.CharField(max_length=50)
    business = models.ForeignKey('accounting.Business', on_delete=models.CASCADE)
    Bkacctno = models.CharField(max_length=64, null=True, blank=True)
    Bkname = models.CharField(max_length=32, null=True, blank=True)
    Bkdate = models.DateField()
    Bkjukyo = models.CharField(max_length=60)
    Bkinput = models.BigIntegerField()
    Bkoutput = models.BigIntegerField()
    Bkjango = models.BigIntegerField()
    regdatetime = models.DateTimeField()
    item = models.ForeignKey('accounting.Item', on_delete = models.PROTECT, null=True)
    subdivision = models.ForeignKey('accounting.Subdivision',on_delete = models.PROTECT, null=True, blank=True)
    relative_subsection = models.ForeignKey('accounting.Subsection', on_delete = models.PROTECT, null=True, blank=True)
    relative_item = models.ForeignKey('accounting.Item', on_delete = models.PROTECT, related_name="relative_item", null=True, blank=True)
    remark = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.Bkid)


class Setting(models.Model):
    name = models.CharField(max_length=15)
    value = models.IntegerField()
    
    def __str__(self):
        return self.name


class Budget(models.Model):
    class Meta:
        unique_together = (('business', 'year', 'type', 'item'),)
    
    business = models.ForeignKey('accounting.Business', on_delete = models.CASCADE)
    year = models.IntegerField()
    type = models.CharField(max_length=27)
    item = models.ForeignKey('accounting.Item', on_delete = models.PROTECT)
    price = models.BigIntegerField(null=True, blank=True)
    row = models.IntegerField()
    context = models.TextField(null=True, blank=True)
    unit_price = models.TextField(null=True, blank=True)
    cnt = models.TextField(null=True, blank=True)
    months = models.TextField(null=True, blank=True)
    percent = models.TextField(null=True, blank=True)
    sub_price = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.item.context


class Menu(models.Model):
    class Meta:
        unique_together = (('business_type', 'url'),)

    name = models.CharField(max_length=10)
    business_type = models.ForeignKey('accounting.Business', on_delete = models.CASCADE)
    url = models.CharField(max_length=30)
    depth = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    has_child = models.BooleanField(default=False)
    parent = models.ForeignKey('accounting.Menu', on_delete=models.SET_NULL, null=True)
    target = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Deadline(models.Model):
    business = models.ForeignKey('accounting.Business', on_delete = models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    regdatetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s_%s" % (self.year, self.month)

import os
class UploadFile(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def delete(self):
        os.remove(self.file.path)
        return super(UploadFile, self).delete()

    def __str__(self):
        return self.title
