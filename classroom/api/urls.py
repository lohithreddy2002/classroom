from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_room', views.create_room,name = "create room"),
    path('get_rooms',views.get_rooms,name="get rooms"),
    path("join_room",views.join_room,name="join room"),
    path("get_contacts",views.get_contacts,name="get contacts"),
    path("create_chat",views.create_chat,name = "create_chat")
]