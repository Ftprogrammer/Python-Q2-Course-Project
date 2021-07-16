from django.contrib import admin

# Register your models here.
from appi.models import UserInfo,Product,AddToCart,Order

admin.site.register(UserInfo)

admin.site.register(Product)
admin.site.register(AddToCart)
admin.site.register(Order)
