from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('subscription/', views.subscription, name='subscription'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('routines/', views.routines, name='routines'),
]