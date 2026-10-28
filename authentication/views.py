from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def login_user(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('/')
    #     else:
    #         messages.success(request, 'Username OR password is incorrect')
    #         return redirect('login')
    return render(request,'auth/login.html')

def logout_user(request):
    # logout(request)
    # messages.success(request, 'logged out')
    return redirect('login')

def register_user(request):

    return render(request, 'auth/register.html')
