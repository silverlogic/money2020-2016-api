from django.db import models


class VendingMachine(models.Model):
    name = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)


class Product(models.Model):
    machine = models.ForeignKey('VendingMachine')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_identifier = models.CharField(max_length=100)
