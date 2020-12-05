# Generated by Django 3.1.3 on 2020-12-05 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_bankaccount_bankid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='transaction_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
