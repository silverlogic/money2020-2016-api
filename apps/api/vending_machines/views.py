from mastercardapicore import RequestMap
from mastercardvending import Machine
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from apps.vending_machines.models import Product

from .serializers import ProductSerializer


class VendingMachinesViewSet(mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    def get_queryset(self):
        return None

    def list(self, request, *args, **kwargs):
        mapObj = RequestMap()
        mapObj.set("latitude", request.data.get('lat', "36.121399"))
        mapObj.set("longitude", request.data.get('long', "-115.169696"))

        responseList = Machine.listByCriteria(mapObj)

        return Response([{
            'name': response.get('name'),
            'description': response.get('description'),
            'address': response.get('address'),
            'distance': response.get('distance'),
            'latitude': response.get('latitude'),
            'longitude': response.get('longitude'),
            'model': response.get('model'),
            'serial': response.get('serial'),
            'serviceId': response.get('serviceId'),
            'products': [ProductSerializer(instance=i).data for i in Product.objects.filter(machine__serial=response.get('serial'))],
        } for response in responseList.get('list')])
