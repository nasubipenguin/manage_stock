# Generated by Django 2.0.9 on 2019-12-15 04:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0020_auto_20191215_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
