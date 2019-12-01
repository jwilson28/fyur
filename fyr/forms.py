from django import forms
from .models import Events, Address, Band, Venue

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'event_start', 'duration_description']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['venue'] = forms.ModelChoiceField(Venue.objects.all())
        self.fields['bands'] = forms.ModelChoiceField(Band.objects.all())


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['house_apt_unit_no','descriptor', 'street', 'street_no',
                  'city', 'state_prov', 'postal_code', 'country']


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'