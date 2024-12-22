from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post


# Create your views here.
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
