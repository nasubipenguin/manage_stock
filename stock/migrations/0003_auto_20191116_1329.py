# Generated by Django 2.2.6 on 2019-11-16 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20191116_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performance',
            old_name='published_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='shikiho',
            old_name='published_date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='published_date',
            new_name='updated_date',
        ),
    ]
