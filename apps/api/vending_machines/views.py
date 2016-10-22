from mastercardapicore import Config, OAuthAuthentication, RequestMap
from mastercardvending import Machine
from rest_framework import mixins, viewsets
from rest_framework.response import Response


class VendingMachinesViewSet(mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    def get_queryset(self):
        return None

    def list(self, request, *args, **kwargs):
        consumerKey = "IVzQ9DSGMDoFaTZTFESpCh3lijeE5xI68L1d0sA_bffd6b00!02324594db1a40fab12eada7da2fef0d0000000000000000"
        keyStorePath = "./test_sandbox.p12"
        keyAlias = "keyalias"
        keyPassword = "keystorepassword"

        auth = OAuthAuthentication(consumerKey, keyStorePath, keyAlias, keyPassword)
        Config.setAuthentication(auth)
        Config.setSandbox(True)   # For production: use Config.setSandbox(false)

        mapObj = RequestMap()
        mapObj.set("latitude", "36.121399")
        mapObj.set("longitude", "-115.169696")

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
        } for response in responseList.get('list')])
