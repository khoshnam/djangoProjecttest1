# Generated by Django 5.1.3 on 2024-12-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_premiumcollection_collection_date1'),
    ]

    operations = [
        migrations.AddField(
            model_name='premiumcollection',
            name='collection_date2',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ'),
        ),
    ]
