from django.db import models


class Product(models.Model):
    ean13 = models.CharField(max_length=13)
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    price = models.FloatField()
    base_price = models.FloatField(null=True)
    tax_percent = models.IntegerField()
    in_stock = models.IntegerField(default=1)
