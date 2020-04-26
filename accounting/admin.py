from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Owner, Business, Sales, Agency, Bank, Level, Account
from .models import Subsection, Paragraph, Item, Subdivision, Transaction, Business_type, TBLBANK, UploadFile, Deadline

# Register your models here.
admin.site.register(Profile)
admin.site.register(Owner)
admin.site.register(Business)
admin.site.register(Sales)
admin.site.register(Agency)
admin.site.register(Account)
admin.site.register(Business_type)
admin.site.register(UploadFile)
admin.site.register(Deadline)

@admin.register(Level)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['level', 'name']
    list_display_links = ['level', 'name']

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    list_display_links = ['code', 'name']
    ordering = ('code',)

@admin.register(Subsection)
class BankAdmin(admin.ModelAdmin):
    ordering = ('institution', 'code')

@admin.register(Paragraph)
class BankAdmin(admin.ModelAdmin):
    ordering = ('subsection', 'code',)

@admin.register(Item)
class BankAdmin(admin.ModelAdmin):
    ordering = ('paragraph', 'code',)

@admin.register(Subdivision)
class BankAdmin(admin.ModelAdmin):
    ordering = ('item', 'code',)

@admin.register(Transaction)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'business', 'Bkid', 'Bkdivision', 'Bkacctno', 'Bkname', 'Bkdate', 'Bkjukyo', 'Bkinput', 'Bkoutput', 'Bkjango', 'regdatetime']

@admin.register(TBLBANK)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'Bkid', 'Bkdivision', 'Bkacctno', 'Bkname', 'Bkdate', 'Bkjukyo', 'sub_Bkjukyo', 'Bkinput', 'Bkoutput', 'Bkjango', 'regdatetime']
