
from django.contrib import admin
from .models import Events, Venue, Event, Review, Comment

# Register your models here.
admin.site.register(Events)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone')
	ordering = ('name',)
	search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	fields = (('name', 'venue'), 'event_date', 'description', 'manager', 'attendees', 'max_attendees', 'event_image')
	list_display = ('name', 'event_date', 'venue')
	list_filter = ('event_date', 'venue')
	ordering = ('event_date',)

@admin.register(Review)
class EventAdmin(admin.ModelAdmin):
	fields = ('title', 'content', 'author')
	list_display = ('title', 'content', 'author')
	list_filter = ('title', 'content', 'author')
	ordering = ('created_at',)

@admin.register(Comment)
class EventAdmin(admin.ModelAdmin):
	fields = ('review', 'author', 'content')
	list_display = ('review', 'author', 'content')
	list_filter = ('review', 'author', 'content')
	ordering = ('created_at',)
