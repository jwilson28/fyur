from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Events, Address, Band, Venue


def index(request):
    events = Events.objects.order_by('-event_start')
    context = {
        'events':events
    }
    return render(request, 'fyr/index.html', context)

def event_detail(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    context = {
        'event': event
    }
    return render(request, 'fyr/event_detail.html', context)

def add_event(request):
    return HttpResponse(request, 'fyr/add_event.html')