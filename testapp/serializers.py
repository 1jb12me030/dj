from .models import *

from rest_framework import serializers


#from rest_framework.serializers import ModelSerializer


class RegistrationSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)

