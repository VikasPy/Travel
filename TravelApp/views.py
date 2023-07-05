from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate


# Create your views here.


def Home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:

            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exist')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exist')
                return redirect('signup')
            else:
                User(username=username,
                    email=email, password=password).save()
                return redirect('login')
        else:
            messages.error(request, 'password does not match')
            return render(request, 'signup.html')

    return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, User)
            messages.success(request, 'login sucessfuly')
            return redirect('home')
        else:
            messages.error(request, 'invalid entry')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
