from django.db import models

from apps.base.models import random_name_in


class PaymentMethod(models.Model):
    user = models.ForeignKey('users.User')
    icon = models.ImageField(upload_to=random_name_in('payments-payment-method-icons'))
