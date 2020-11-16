from django.db import models
from django.contrib.auth.models import User

from store.models import Product


class Order(models.Model):
    delivery_address = models.TextField(default="")
    base = models.FloatField(null=True)
    taxes = models.FloatField(null=True)
    total_amount = models.FloatField()
    note = models.TextField(null=True)
    is_sent = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product, through='OrderProduct')


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
