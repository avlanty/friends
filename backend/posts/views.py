from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='signin')
def create_post(request):
    return render(request, "posts/create.html")