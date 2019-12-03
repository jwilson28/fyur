from django.contrib import admin

from .models import Venue, Band, Event, Address

admin.site.register(Band)
admin.site.register(Event)
admin.site.register(Address)
admin.site.register(Venue)
