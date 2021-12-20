from django.db import models
from django.db.models.deletion import CASCADE
from rest_framework import authentication
from django.db import models
from classroom.settings import AUTH_USER_MODEL
# Create your models here.

# class Room(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     user = models.ForeignKey(User,on_delete=models.CASCADE,db_column="user_id")
#     room_id = models.CharField(max_length=10)
#     subject = models.CharField(max_length=30,blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=CASCADE, related_name='friends')
    friends = models.ManyToManyField('self',blank=True)
    
class Message(models.Model):
    user = models.ForeignKey(Contact,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)



class Chat(models.Model):
    participants = models.ManyToManyField(Contact,blank=True)
    messages = models.ManyToManyField(Message,blank=True)
