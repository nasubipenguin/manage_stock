# Generated by Django 2.0.9 on 2019-11-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0017_auto_20191126_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shikiho',
            name='market_capitalization',
            field=models.FloatField(),
        ),
    ]
