# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from service.quickstart.serializers import MessageSerializer, AccountSerializer
from service.quickstart.models import Account, Message


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and sending messages to WhatsApp.
    """
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint for adding new WhatsApp accounts to the service.
    """
    queryset = Account.objects.all().order_by('-created')
    serializer_class = AccountSerializer
