from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

from datetime import date

class UserInfo(models.Model):

    CHOICES = [
        ('admin', 'admin'),
        ('suser', 'suser'),

    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=CHOICES)



class Product(models.Model):
    product_id = models.AutoField(primary_key=True, unique=True)
    product_name = models.CharField(max_length=20)
    product_description = models.CharField(max_length=100,blank=True,null=True)
    product_prepare_time = models.IntegerField()
    product_price = models.IntegerField(default=0)
    created_time = models.DateTimeField(default=date.today())

    def __str__(self):
        """String for representing the Model object."""
        return self.product_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this product."""
        return reverse('product-detail', args=[str(self.product_id)])



class AddToCart(models.Model):
    cart_id = models.AutoField(primary_key=True, unique=True)
    id_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    @property
    def total_cost_cart(self):
        return self.quantity * self.id_product.product_price


class Order(models.Model):
    order_id = models.AutoField(primary_key=True, unique=True)
    id_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=date.today())
    total_price=models.IntegerField(default=0)
    @property
    def total_cost(self):
        return self.quantity * self.id_product.product_price

