# Generated by Django 2.2.7 on 2019-12-18 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0023_auto_20191218_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='high_limit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='low_limit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
