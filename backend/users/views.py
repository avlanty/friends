from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from .models import Member

# Create your views here.
def home(request):
    return render(request, "users/home.html")

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
            return redirect("signin")
        
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
            return redirect("profile")
        else:
            messages.error(request, ('Incorrect email or password, please try again.'))
            return render(request, "users/signin.html", {'username':username,
                                                        'password':password},)
    else:
        return render(request, "users/signin.html")
    

def sign_out(request):
    logout(request)
    return redirect("home")


@login_required(login_url='signin')
def profile(request):
    return render(request, "users/profile.html")


@login_required(login_url='signin')
def profile_edit(request):
    if request.method == "POST":
        upload = request.FILES.get('upload', None)
        bio = request.POST.get('bio', '')
        date_of_birth = request.POST.get('date_of_birth', '')

        profile = request.user.profile
        profile.bio = bio

        if upload:
            profile.profile_picture = upload

        try:
            if date_of_birth:
                parsed_date = parse_date(date_of_birth)
                if not parsed_date:
                    raise ValidationError('Invalid date format. Please use YYYY-MM-DD.')
                profile.date_of_birth = parsed_date

            profile.save()
            messages.success(request, 'Profile updated!')

        except ValidationError:
            messages.error(request, 'Error updating profile. Please try again.')
            return render(request, 'users/profileedit.html', {'bio':bio, 'date_of_birth':date_of_birth, 'upload':upload})

        return redirect('profile')
    return render(request, 'users/profileedit.html')