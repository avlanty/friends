from django.shortcuts import render
from posts.models import Post
from users.models import Member

# Create your views here.
def home(request):
    posts = Post.objects.all()
    members = Member.objects.all()
    return render(request, 'core/home.html', {'posts': posts,
                                              'members': members,})

