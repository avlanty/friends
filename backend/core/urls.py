from django.urls import path, include
from . import views

urlPatterns = [
    path('', views.home, name="home"),
]