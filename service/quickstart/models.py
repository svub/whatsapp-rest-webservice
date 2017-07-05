# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from service.quickstart.whatsapp import WhatsApp

# Create your models here.

class Account(models.Model):

    """
    A WhatsApp account to be used to send messages from
    """

    label = models.CharField(
        max_length=200,
        help_text='A name for this account to help identify the owner.'
    )

    cc = models.CharField(
        max_length=3,
        default=49,
        help_text='Country code without +'
    )

    phone = models.CharField(
        max_length=30,
        help_text='Full phone number with country code but without +',
        primary_key=True
    )

    sms_code = models.CharField(
        max_length=7,
        help_text='The code received via SMS during registration xxx-xxx.',
    )

    api_password = models.CharField(
        max_length=50,
        help_text='The account password required to use the WhatsApp service. Automatically generated when creating and registering a new account.',
    )

    # cf. https://en.wikipedia.org/wiki/Mobile_country_code
    MOBILE_COUNTRY_CODES = (
        (26203, 'O2'),
        (26201, 'Telekom'),
        (26202, 'Vodafone')
    )

    mcc = models.IntegerField(
        choices = MOBILE_COUNTRY_CODES,
        help_text='The mobile phone provider you are using.'
    )

    created = models.DateTimeField(
        help_text = 'Time when account was added.',
        # set to 'now' when sending new message
        auto_now_add=True
    )


class Message(models.Model):

    """
    A message to sent or to be send via WhatsApp
    """

    origin = models.CharField(
        max_length=30,
        default='',
        help_text='Phone number of WhatsApp account owner - ignored for now.'
    )

    target = models.CharField(
        max_length=50,
        help_text='Group ID or full phone number of recepient with country code but without +'
    )

    body = models.CharField(
        help_text='Message text',
        max_length=500
    )

    timestamp = models.DateTimeField(
        help_text = 'Time when message has been sent.',
        # set to 'now' when sending new message
        auto_now_add=True
    )

    STATUSES = (
        ('U', 'Unsend'),
        ('S', 'Sent'),
        ('A', 'Acknowledged'),
        ('E', 'Error occured trying to send message'),
    )

    status = models.CharField(
        max_length=1,
        default='U',
        choices=STATUSES
    )

    def save(self, *args, **kwargs):
        # hooking up save to actually send message via WhatsApp API
        self.status = 'S' if WhatsApp.send(self.target, self.body)\
                          else 'E'

        super(Message, self).save(*args, **kwargs)
