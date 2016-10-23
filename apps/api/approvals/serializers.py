from mastercardapicore import RequestMap
from mastercardvending import Approval
from rest_framework import serializers


class ApprovalCreateSerializer(serializers.Serializer):
    payload = serializers.CharField()

    def create(self, validated_data):
        mapObj = RequestMap()
        mapObj.set('payload', validated_data['payload'])
        response = Approval.create(mapObj)
        return response

    def to_representation(self, approval):
        return {
            'amount': approval.get('amount'),
            'approvalPayload': approval.get('approvalPayload'),
            'previous': {
                'id': approval.get('previous.id'),
                'state': approval.get('previous.state'),
            },
            'id': approval.get('id'),
            'sessionId': approval.get('sessionId'),
        }


class ApprovalUpdateSerializer(serializers.Serializer):
    id = serializers.CharField()
    payload = serializers.CharField()

    def create(self, validated_data):
        mapObj = RequestMap()
        mapObj.set('id', validated_data['id'])
        mapObj.set('payload', validated_data['payload'])
        response = Approval.update(mapObj)
        return response

    def to_representation(self, approval):
        return {
            'amount': approval.get('amount'),
            'id': approval.get('id'),
            'sessionId': approval.get('sessionId'),
            'state': approval.get('state'),
        }
