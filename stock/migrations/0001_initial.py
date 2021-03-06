# Generated by Django 2.2.6 on 2019-11-04 13:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_code', models.IntegerField(max_length=4, primary_key=True, serialize=False)),
                ('stock_name', models.CharField(max_length=50)),
                ('accounting_month', models.IntegerField(max_length=2)),
                ('business_type', models.CharField(max_length=20)),
                ('ir_url', models.URLField(blank=True, null=True)),
                ('watch_flag', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shikiho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_year', models.IntegerField(max_length=4)),
                ('pub_month', models.IntegerField(max_length=2)),
                ('market_capitalization', models.IntegerField()),
                ('capital_ratio', models.FloatField()),
                ('roe', models.FloatField()),
                ('roa', models.FloatField()),
                ('operating_cf', models.BooleanField()),
                ('investing_cf', models.BooleanField()),
                ('financing_cf', models.BooleanField()),
                ('headline_1', models.CharField(max_length=200)),
                ('headline_2', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('stock_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.IntegerField(max_length=1)),
                ('pub_year', models.IntegerField(max_length=4)),
                ('pub_month', models.IntegerField(max_length=2)),
                ('target_period', models.IntegerField(max_length=4)),
                ('is_established', models.IntegerField(max_length=1)),
                ('sales_amount', models.IntegerField()),
                ('operating_income', models.IntegerField()),
                ('ordinary_income', models.IntegerField()),
                ('net_income', models.IntegerField()),
                ('per', models.FloatField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('stock_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock')),
            ],
        ),
    ]
