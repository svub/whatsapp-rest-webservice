from rest_framework import serializers
from service.quickstart.models import Account, Message


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('label', 'cc', 'phone', 'sms_code', 'api_password', 'mcc')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('origin', 'target', 'body', 'timestamp', 'status')

