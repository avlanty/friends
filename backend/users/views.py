from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.contrib import messages
from .models import Member

# Create your views here.
def home(request):
    return render(request, "users/base.html")

def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        try:
            Member.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            messages.success(request, 'Your account has been created. Welcome to Friends!')
            return redirect("home")
        
        except IntegrityError:
            if Member.objects.filter(username=username).exists() or Member.objects.filter(email=email).exists():
                messages.error(request, 'Username and/or email already exists. Please choose another.')
            return render(request, "users/signup.html", {'first_name': first_name, 
                                                        'last_name': last_name, 
                                                        'username': username, 
                                                        'email': email, 
                                                        'password': password
            })
        
        except Exception:
            messages.error(request, f"You must fill all fields. Please try again.")
            return render(request, "users/signup.html", {'first_name': first_name, 
                                                        'last_name': last_name, 
                                                        'username': username, 
                                                        'email': email, 
                                                        'password': password
            })
    
    else:
        return render(request, "users/signup.html")


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, ('Incorrect email or password, please try again.'))
            return render(request, "users/signin.html", {'username':username,
                                                        'password':password},)
    else:
        return render(request, "users/signin.html")