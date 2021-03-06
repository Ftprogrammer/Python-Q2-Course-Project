# Generated by Django 3.2.5 on 2021-07-13 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=20)),
                ('product_description', models.CharField(blank=True, max_length=100, null=True)),
                ('product_prepare_time', models.IntegerField()),
                ('product_price', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'admin'), ('suser', 'suser')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('quantity', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appi.products')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('quantity', models.IntegerField()),
                ('ordered', models.BooleanField(default=False)),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appi.products')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
