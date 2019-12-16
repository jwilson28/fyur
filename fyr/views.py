from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Event, Address, Band, Venue
from .forms import EventForm, AddressForm, BandForm, VenueForm, CommentForm


def index(request):
    events = Event.objects.order_by('-event_start')
    context = {
        'events':events
    }
    return render(request, 'fyr/index.html', context)

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print("is the form bound or not? (before cleaning data) ", form.is_bound)
        if form.is_valid():
            print("is the form bound or not? (before cleaning data)", form.is_bound)
            pseudonym = form.cleaned_data.get("pseudonym")
            make_public = form.cleaned_data["make_public"]
            comment = form.cleaned_data["comment"]
            comment_deets = {}
            comment_deets["pseudonym"] = pseudonym
            comment_deets["make_public"] = make_public
            comment_deets["comment"] = comment
            return render(request, 'fyr/comment_form.html', {'form':form, 'comment_deets':comment_deets})
    else:
        form = CommentForm()
        print("is the form bound or not? (in the request (before form submission)) ", form.is_bound)
    return render(request, 'fyr/comment_form.html', {'form':form})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event
    }
    return render(request, 'fyr/event_detail.html', context)

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save()
            return HttpResponseRedirect(reverse('fyr:index'))
        else:
            print("Invalid form submission")
    else:
        form = EventForm()
        return render(request, 'fyr/add_event.html', {'form':form})

def address_list(request):
    addresses = Address.objects.order_by('country')
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

def band_list(request):
    bands = Band.objects.order_by('name')
    return render(request, 'fyr/band_list.html', {'bands':bands})

def add_band(request):
    if request.method == 'POST':
        band_form = BandForm(request.POST)
        if band_form.is_valid():
            new_band = band_form.save()
            return HttpResponseRedirect(reverse('fyr:band_list'))
        else:
            return render(request, 'fyr/add_band.html', {'band_form': band_form})
    else:
        band_form = BandForm()
        return render(request, 'fyr/add_band.html', {'band_form':band_form})

def venue_list(request):
    venues = Venue.objects.all().order_by('address__city')
    return render(request, 'fyr/venue_list.html', {'venues':venues})

def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            new_venue = form.save()
            return HttpResponseRedirect(reverse('fyr:venue_list'))
        else:
            return render(request, 'fyr/add_venue.html', {'form': form})
    else:
        form = VenueForm()
        return render(request, 'fyr/add_venue.html', {'form': form})

