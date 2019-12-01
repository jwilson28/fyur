from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Events, Address, Band, Venue
from .forms import EventForm, AddressForm


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

# def add_event(request):
#     if request.method == 'post':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             new_event = form.cleaned_data()
#     return HttpResponse(request, 'fyr/add_event.html')

def address_list(request):
    addresses = Address.objects.order_by('country')
    print(len(addresses), " is the num of addresses...")
    return render(request, 'fyr/address_list.html', {'addresses':addresses})


def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            new_address = form.save()
            return HttpResponseRedirect(reverse('fyr:address_list'))
        else:
            print("Form was NOT valied!!!")
    else:
        form = AddressForm()
        return render(request, 'fyr/add_address.html', {'form':form})