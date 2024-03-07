from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from django.contrib.auth.models import User
from .forms import VenueForm, EventFormAdmin, EventForm
from django.contrib import messages
from django.core.paginator import Paginator


# Homepage calendar view
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
#Query the Event Model For Dates
    event_list = Event.objects.filter(
		event_date__year = year,
		event_date__month = month_number,
		)
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
		'event_list': event_list,
		})

# venue views

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
	#Set up Pagination
	p = Paginator(Venue.objects.all().order_by('name'), 10)
	page = request.GET.get('page')
	venues = p.get_page(page)
	return render(request, 'events/list_venues.html',
		{'venues': venues}
		)

def search_venues(request):
	if request.method == "POST":
		searched = request.POST['searched']
		venues = Venue.objects.filter(name__contains=searched)
		return render(request, 'events/search_venues.html',
		{'searched': searched,
		'venues':venues})
	else:
		return render(request, 'events/search_venues.html',
		{})

def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, request.FILES or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('list-venues')

	return render(request, 'events/update_venue.html',
		{'venue': venue,
		'form': form})

def delete_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue_owner = User.objects.get(pk=venue.owner)
	if request.user == venue_owner or request.user.is_superuser:
		venue.delete()
		messages.success(request, ("Venue Deleted!"))
		return redirect('list-venues')
	else:
		messages.success(request, ("You aren't authorised to do that!"))
		return redirect('list-venues')

# event views

def add_event(request):
	submitted = False
	if request.method == "POST":
		if request.user.is_superuser:
			form = EventFormAdmin(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/add_event?submitted=True')
		else:
			form = EventForm(request.POST)
			if form.is_valid():
				# form.save()
				event = form.save(commit=False)
				event.manager = request.user # logged in user
				event.save()
				return HttpResponseRedirect('/add_event?submitted=True')
	else:
		if request.user.is_superuser:
			form = EventFormAdmin
		else: 
			form = EventForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'events/add_event.html', {'form': form, 'submitted':submitted})

def list_events(request):
	#Set up Pagination
	p = Paginator(Event.objects.all().order_by('event_date'), 3)
	page = request.GET.get('page')
	events = p.get_page(page)
	return render(request, 'events/event.html',
		{'events': events}
		)

def all_events(request):
	events_list = Event.objects.all().order_by('event_date')
	return render(request, 'events/events_list.html',
		{'events_list': events_list})

def show_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	return render(request, 'events/show_event.html',
		{'event': event})

def search_events(request):
	if request.method == "POST":
		searched = request.POST['searched']
		events = Event.objects.filter(name__contains=searched)

		return render(request, 'events/search_events.html',
		{'searched': searched,
		'events':events})
	else:
		return render(request, 'events/search_venues.html',
		{})

def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.user == event.manager or request.user.is_superuser:
		event.delete()
		messages.success(request, ("Event Deleted!"))
		return redirect('list-events')
	else:
		messages.success(request, ("You aren't authorised to do that!"))
		return redirect('list-events')

def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.user.is_superuser:
		form = EventFormAdmin(request.POST or None, instance=event)
	else:
		form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('list-events')
	return render(request, 'events/update_event.html',
		{'event': event,
		'form': form})

def attend_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	if event.max_attendees == 0 or event.attendees.count() < event.max_attendees:
		if request.method == 'POST':
			event.attendees.add(request.user)
			return redirect('list-events')
	else:
		messages.success(request, "Sorry, this event is already fully booked!")
	return redirect('list-events')
	
def cancel_attendance(request, event_id):
	event = Event.objects.get(pk=event_id)
	if request.method == 'POST':
		event.attendees.remove(request.user)
		return redirect('list-events')

def my_events(request):
	if request.user.is_authenticated:
		me = request.user.id
		events = Event.objects.filter(attendees=me)
		return render(request, 'events/my_events.html', {
			'events':events,
			'messages': messages.get_messages(request),
			})
	else:
		return redirect('index')
		messages.success(request, "You aren't authorised to view this page.")
