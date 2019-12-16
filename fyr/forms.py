from django import forms
from .models import Event, Address, Band, Venue

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'event_start', 'duration_description']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['venue'] = forms.ModelChoiceField(Venue.objects.all())
        self.fields['bands'] = forms.ModelMultipleChoiceField(Band.objects.all())


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['house_apt_unit_no','descriptor', 'street', 'street_no',
                  'city', 'state_prov', 'postal_code', 'country']


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'

class CommentForm(forms.Form):
    pseudonym = forms.CharField(label='What do you go by? ', max_length=100)
    #comment = forms.Textarea(label='Add comment here')
    comment = forms.CharField(label='Type comment', widget=forms.Textarea)
    make_public = forms.BooleanField(required=False)

