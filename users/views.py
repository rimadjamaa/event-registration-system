from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from .models import Event,Registration
# Create your views here.

def register_view(request):
    if request.method == "POST":
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created .")
            return redirect('login')
    else:
      form = CustomUserCreationForm()
    return render(request,'users/register.html', {"form" : form})


def login_view(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "failed to login .")
            return redirect('login')
    return render(request,'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def RegisterEvent_view(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.event = event
            registration.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'users/REvent.html', {'form': form, 'event': event})


@login_required(login_url='login')
def user_registrations_view(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'users/user_registrations.html', {'registrations': registrations})