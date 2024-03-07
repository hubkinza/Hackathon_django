from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Events, Venue
from django.contrib.auth.models import User
from .forms import VenueForm
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def index(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = request.user
    month = month.capitalize()
# Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number - int(month_number)
# create a calendar
    cal = HTMLCalendar().formatmonth(
		year, 
		month_number)
# Get current year
    now = datetime.now() 
    current_year = now.year
#Query the Events Model For Dates
    # event_list = Event.objects.filter(
	# 	event_date__year = year,
	# 	event_date__month = month_number,
	# 	)
# Get current time
    time = now.strftime('%H:%M:%S %p')

    return render(request, 'events/index.html', {
		'name': name,
		'year': year,
		'month': month,
		'month_number': month_number,
		'cal': cal,
		'current_year': current_year,
		'time' : time,
		# 'event_list': event_list,
		})

def add_venue(request):
	submitted = False
	if request.method == 'POST':
		form = VenueForm(request.POST, request.FILES)
		if form.is_valid():
			venue = form.save(commit=False)
			venue.owner = request.user.id # logged in user
			venue.save()
			return HttpResponseRedirect('/add_venue?submitted=True') 
	else: 
		form = VenueForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'events/add_venue.html', {'form': form, 'submitted':submitted})

def show_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue_owner = User.objects.get(pk=venue.owner)
	return render(request, 'events/show_venue.html',
		{'venue': venue,
		'venue_owner': venue_owner})

def list_venues(request):
	# venue_list = Venue.objects.all().order_by('name')

	#Set up Pagination
	p = Paginator(Venue.objects.all().order_by('name'), 10)
	page = request.GET.get('page')
	venues = p.get_page(page)
	return render(request, 'events/list_venues.html',
		{'venues': venues}
		)
