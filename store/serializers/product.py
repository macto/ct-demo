from rest_framework import serializers
from store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "ean13", "name", "price", "base_price", "tax_percent", "in_stock"]

