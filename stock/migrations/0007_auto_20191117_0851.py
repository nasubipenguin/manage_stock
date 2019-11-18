# Generated by Django 2.2.6 on 2019-11-16 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20191116_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='stock_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stock.Stock'),
        ),
        migrations.AlterField(
            model_name='shikiho',
            name='headline_1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shikiho',
            name='headline_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shikiho',
            name='stock_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stock.Stock'),
        ),
    ]
