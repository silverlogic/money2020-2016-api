from rest_framework import serializers

from apps.vending_machines.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_identifier', 'name', 'price',)
