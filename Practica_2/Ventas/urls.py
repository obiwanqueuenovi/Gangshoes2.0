from django.contrib import admin
from django.urls import path
from .views import home,inicio,mascota

urlpatterns = [
    path('home/',home,name="home"),
    path('',inicio,name="inicio"),
    path('mascota',mascota,name="mascota"),
]