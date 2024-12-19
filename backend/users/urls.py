from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sign-up/', views.sign_up, name="signup"),
    path('sign-in/', views.sign_in, name="signin"),
    path('sign-out/', views.sign_out, name="signout"),
]