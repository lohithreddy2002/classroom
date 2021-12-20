from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.contrib.auth.models import User
from classroom.settings import AUTH_USER_MODEL
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from api.models import Contact

User = get_user_model()

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def Signup(request):
    email = request.data["email"]
    password = request.data["password"]
    user = User(email = email,password = password)
    try:
        user.save()
    except IntegrityError:
        data = {
            "data":"email already exists"
        }
        return Response(data, status=HttpResponseBadRequest.status_code)
    token = Token.objects.create(user =user)
    contact = Contact(user = user)
    contact.save()
    data = { 
     "token" :token.key,
     "test" : user.id
    }
    return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data["email"]
    password = request.data["password"]
    try:
        user = User.objects.get(email= username)
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
        return Response(data,HttpResponseBadRequest.status_code)

