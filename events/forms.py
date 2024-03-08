from django import forms
from django.forms import ModelForm
from .models import Venue, Event, Review, Comment

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

# SuperUser Event Form
class EventFormAdmin(ModelForm):
	class Meta:
		model = Event
		fields =  ('name', 'event_date', 'venue', 'manager', 'description', 'attendees', 'max_attendees', 'event_image')
		labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Venue',
			'manager': 'Event Manager',
			'description': '',
			'attendees': 'Attendees',
			'event_image': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
			'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
			'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
			'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event Manager'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About Event'}),
			'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
		}

# User Event Form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields =  ('name', 'event_date', 'venue', 'description', 'attendees', 'max_attendees', 'event_image')
		labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Venue',
			'description': '',
			'attendees': 'Attendees',
		 	'max_attendees': 'Maximum Attendees',
			'event_image': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
			'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
			'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About Event'}),
			'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
			'max_attendees' : forms.NumberInput(attrs={'min': 0})
		}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']