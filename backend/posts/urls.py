from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name="createpost"),
    path('delete/<int:post_id>/', views.delete_post, name="deletepost"),
    path('api/posts/', views.PostListAPIView.as_view(), name="postlist"),
]