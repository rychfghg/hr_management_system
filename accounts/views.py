# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def home_view(request):
    return render(request, 'accounts/home.html')  



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'accounts/login.html') 

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('home') 
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'accounts/register.html')  

def home_view(request):
    return render(request, 'accounts/home.html')  
