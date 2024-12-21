from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name="signup"),
    path('sign-in/', views.sign_in, name="signin"),
    path('sign-out/', views.sign_out, name="signout"),
    path('profile/', views.profile, name="profile"),
    path('profile/edit', views.profile_edit, name="edit"),
]