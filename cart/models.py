from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from products.models import Product

# Create your models here.

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE , 'Live'), (DELETE , 'Delete'))
    CART_STAGE = 0
    order_status= models.IntegerField(default=CART_STAGE)
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderedItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='added_carts')
    qty = models.IntegerField(default=1)
    owner = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
