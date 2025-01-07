from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import PostSerializer


# Create your views here.
# Existing HTML views

@login_required(login_url='signin')
def create_post(request):
    if request.method == "POST":
        content = request.POST.get('content', '')
        
        if content:
            try:
                Post.objects.create(user=request.user, content=content)
                messages.success(request, 'Post created!')

            except Exception:
                messages.error(request, 'Post creation failed, please try again.')
                return render(request, "posts/create.html", {'posts': content})
        
        return redirect("home")

    return render(request, "posts/create.html")


@login_required(login_url='signin')
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        messages.success(request, 'Post deleted!')

    except Exception:
        messages.error(request, 'Failed to delete post, try again.')
    
    return redirect("home")


# New API views

class PostListAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
