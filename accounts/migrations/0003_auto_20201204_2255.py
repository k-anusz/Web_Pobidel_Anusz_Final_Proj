# Generated by Django 3.1.3 on 2020-12-05 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_bankaccount_banks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Banks',
            new_name='Bank',
        ),
    ]
