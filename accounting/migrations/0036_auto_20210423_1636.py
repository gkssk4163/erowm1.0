# Generated by Django 2.1.4 on 2021-04-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0035_business_business_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='remark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
