from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def Signup(request):
    email = request.data["email"]
    password = request.data["password"]
    user = User(username = email,password = password)
    user.save()
    token = Token.objects.create(user =user)
    data = { 
     "token" :token.key,
     "test" : user.id
    }
    return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data["username"]
    password = request.data["password"]
    try:
        user = User.objects.get(username = username)
        print(user.id)
        token = Token.objects.get(user = user)
        print(token.key)
        data = {
        "user_id":user.id,
        "token": token.key,
        }
        return Response(data)
    except:
        data = {
            "message" : "no user found"
        }
        return Response(data)
