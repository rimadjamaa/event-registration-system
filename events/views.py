from django.shortcuts import render, get_object_or_404, redirect
from .models import Event


# Create your views here.

def homepage(request):
    events = Event.objects.all()
    return render(request,'events/homepage.html', {'events': events})

def event_detail_view(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})

