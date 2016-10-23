from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.payments.models import PaymentMethod

from .serializers import PaymentMethodSerializer


class PaymentMethodsViewSet(mixins.ListModelMixin,
                            GenericViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classses = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        queryset = super(PaymentMethodsViewSet, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
