from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_room', views.create_room,name = "create room"),
    path('get_rooms',views.get_rooms,name="get rooms"),
    path("join_room",views.join_room,name="join room"),
]