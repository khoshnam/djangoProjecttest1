# Generated by Django 5.1.3 on 2024-12-17 17:53

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_premiumcollection_collection_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='premiumcollection',
            name='collection_date1',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='تاریخ وصول'),
        ),
    ]