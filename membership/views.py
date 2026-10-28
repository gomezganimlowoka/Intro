from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'membership/home.html')

def profile(request):
    return render(request, 'membership/profile.html')

def subscription(request):
    return render(request, 'membership/subscription.html')

def dashboard(request):
    return render(request, 'membership/dashboard.html')

def routines(request):
    return render(request, 'membership/routines.html')


