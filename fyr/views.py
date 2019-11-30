from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Events, Address, Band, Venue


def index(request):
    events = Events.objects.order_by('-event_start')
    context = {
        'events':events
    }
    return render(request, 'index.html', context)