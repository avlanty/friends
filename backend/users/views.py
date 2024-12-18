from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MemberForm

# Create your views here.
def home(request):
    return render(request, "users/base.html")

def sign_up(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            username = request.POST['user_name']
            email = request.POST['email']
            password = request.POST['email']
            messages.error(request, ('Your form is invalid, please try again.'))
            return render(request, "users/signup.html", {'firstname':firstname,
                                                         'lastname':lastname,
                                                         'username':username,
                                                         'email':email,
                                                         'password':password},)
        messages.success(request, ('Form submitted. Thank you for joining Friends!'))
        return redirect("home")
    else:
        return render(request, "users/signup.html")