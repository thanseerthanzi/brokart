from django.db import models
from customers.models import customer
from products.models import Product

# Model for cart orders

class Order(models.Model):
    LIVE=1 
    DELETE=0
    DELETE_CHOICE=((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERD=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (ORDER_DELIVERD,"ORDER_DELIVERD"),
                   (ORDER_REJECTED,"ORDER_REJECTED")
                   )

    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True, related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) 

class Ordereditem(models.Model):
    products=models.ForeignKey(Product,related_name='add_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')

