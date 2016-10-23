from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import ApprovalCreateSerializer, ApprovalUpdateSerializer


class ApprovalCreateViewSet(mixins.CreateModelMixin,
                            GenericViewSet):
    serializer_class = ApprovalCreateSerializer

    def get_queryset(self):
        return None


class ApprovalUpdateViewSet(mixins.CreateModelMixin,
                            GenericViewSet):
    serializer_class = ApprovalUpdateSerializer

    def get_queryset(self):
        return None
