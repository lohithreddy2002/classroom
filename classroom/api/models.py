from django.db import models
from django.db.models.deletion import CASCADE
from rest_framework import authentication
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,db_column="user_id")
    room_id = models.CharField(max_length=10)
    subject = models.CharField(max_length=30,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserRoom(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE)


class RoomPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    file = models.CharField(max_length=100)
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE,db_column="room_id")
    # created_at = models.DateTimeField(auto_now_add=True)
    # post_type = models.IntegerField()
    # should_post_at = models.DateTimeField()
