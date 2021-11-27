from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
import random
from rest_framework.response import Response
import string
from . import serializers
from . import models
 

# Create your views here.

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_room(request):
    name = request.data["name"]
    subject = request.data["subject"]
    host = request.user
    print(host)
    chars = string.ascii_letters + string.digits
    room_id = random_string_generator(10, chars)
    room = models.Room(name= name,user = host,room_id =room_id,subject = subject)
    room.save()
    data = {
        "message":"room created successfully"
    }
    return Response(data=data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_rooms(request):
    rooms_db = models.Room.objects.filter(user = request.user)
    rooms = []
    da = models.UserRoom.objects.filter(user_id = request.user)
    for i in da:
        mod = models.Room.objects.get(id = i.room_id.id)
        rooms.append(serializers.RoomSerializer(mod).data)
    for i in rooms_db:
        rooms.append(serializers.RoomSerializer(i).data)
    data = {
        "rooms":rooms
    }
    return Response(data=data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    description = request.data[""]
    room_id = request.data["room_id"]
    room = models.Room.objects.get(id = room_id)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_room(request):
    try:
        room_id = request.data["room_id"]
    except:
        data = {
        "message":"room_id expected"
        }
        return Response(data=data,status=400)
    room = models.Room.objects.get(room_id = room_id)
    if(room.user.id == request.user.id):
        data = {
        "message":"joined room successfully"
        }
        return Response(data=data)
    models.UserRoom(room_id = room,user_id = request.user).save()
    data = {
        "message":"joined room successfully"
    }
    return Response(data=data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_joined_rooms(request):
    a = models.UserRoom.objects.filter(request.user)
    print(a)