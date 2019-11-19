# Generated by Django 2.2.6 on 2019-11-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_auto_20191118_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_code',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='performance',
            unique_together={('stock_code', 'source', 'pub_year', 'pub_month', 'target_period')},
        ),
    ]