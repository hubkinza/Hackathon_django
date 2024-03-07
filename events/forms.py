from django import forms
from django.forms import ModelForm
from .models import Venue, Event

# Create a venue form
class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields =  ('name', 'address', 'postcode', 'phone', 'web', 'email_address', 'venue_image')
		labels = {
			'name': '',
			'address': '',
			'postcode': '',
			'phone': '',
			'web': '',
			'email_address': '',
			'venue_image': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
			'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
			'postcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postcode'}),
			'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
			'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website Link'}),
			'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
		}