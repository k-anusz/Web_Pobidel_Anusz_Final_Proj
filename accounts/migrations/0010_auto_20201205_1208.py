# Generated by Django 3.1.3 on 2020-12-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20201205_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='bankId',
        ),
        migrations.AddField(
            model_name='bank',
            name='id',
            field=models.AutoField(auto_created=True, default=22, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]