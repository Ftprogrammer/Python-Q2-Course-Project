# Generated by Django 3.2.5 on 2021-07-13 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0002_order_total_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]