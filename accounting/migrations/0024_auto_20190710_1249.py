# Generated by Django 2.1.4 on 2019-07-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0023_auto_20190417_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='webid',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='webpw',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
