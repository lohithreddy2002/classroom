from django.db.models import fields
from rest_framework import serializers
from . import models

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomPost
        fields = '__all__'