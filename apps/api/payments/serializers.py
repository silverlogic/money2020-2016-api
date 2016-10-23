from rest_framework import serializers

from apps.payments.models import PaymentMethod

from ..fields import ThumbnailImageField


class PaymentMethodSerializer(serializers.ModelSerializer):
    icon = ThumbnailImageField()

    class Meta:
        model = PaymentMethod
        fields = ('id', 'icon',)
