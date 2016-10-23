from django.contrib import admin

from .models import Product, VendingMachine

admin.site.register(VendingMachine)
admin.site.register(Product)
