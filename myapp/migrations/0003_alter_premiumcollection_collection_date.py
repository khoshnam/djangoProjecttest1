# Generated by Django 5.1.3 on 2024-12-01 15:57

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_contracts_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premiumcollection',
            name='collection_date',
            field=django_jalali.db.models.jDateField(auto_now_add=True, null=True, verbose_name='تاریخ وصول'),
        ),
    ]
