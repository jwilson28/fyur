from django.contrib import admin

from .models import Venue, Band, Events, Address

admin.site.register(Band)
admin.site.register(Events)
admin.site.register(Address)
admin.site.register(Venue)
