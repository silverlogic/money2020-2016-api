from rest_framework import serializers

from apps.vending_machines.models import Product

from ..fields import ThumbnailImageField


class ProductSerializer(serializers.ModelSerializer):
    icon = ThumbnailImageField()

    class Meta:
        model = Product
        fields = ('product_identifier', 'name', 'icon', 'price',)
