# Generated by Django 2.0.9 on 2019-11-24 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_auto_20191121_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='net_income_yoy',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='performance',
            name='operating_income_yoy',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='performance',
            name='ordinary_income_yoy',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='performance',
            name='sales_amount_yoy',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
