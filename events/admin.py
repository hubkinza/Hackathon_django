
from django.contrib import admin
from .models import Events
from .models import Venue

# Register your models here.
admin.site.register(Events)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'phone')
	ordering = ('name',)
	search_fields = ('name', 'address')