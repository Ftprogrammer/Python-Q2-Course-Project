# Generated by Django 3.2.5 on 2021-07-13 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0003_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_time',
            field=models.DateTimeField(default=datetime.date(2021, 7, 13)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_time',
            field=models.DateTimeField(default=datetime.date(2021, 7, 13)),
        ),
    ]
