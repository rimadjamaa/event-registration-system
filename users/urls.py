from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.register_view ,name='register'),    
    path('login/', views.login_view ,name='login'),
    path('logout/', views.logout_view ,name='logout'),
    path('RegisterEvent/<int:id>/', views.RegisterEvent_view ,name='REvent'),
      path('registrations/', views.user_registrations_view, name='user_registrations')
]