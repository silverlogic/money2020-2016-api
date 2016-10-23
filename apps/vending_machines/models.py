from django.db import models

from apps.base.models import random_name_in


class VendingMachine(models.Model):
    name = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    machine = models.ForeignKey('VendingMachine')
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to=random_name_in('product-icons'))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_identifier = models.CharField(max_length=100)

    def __str__(self):
        return self.name
