# Generated by Django 2.1.4 on 2021-02-09 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0031_auto_20210209_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='stamp',
            new_name='manager_stamp',
        ),
    ]