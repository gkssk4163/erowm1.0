# Generated by Django 2.1.4 on 2021-02-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0030_account_account_yn'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='ceo_stamp',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='business',
            name='stamp',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
