from django.db.models import fields
from rest_framework import serializers
from . import models

# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Room
#         fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'