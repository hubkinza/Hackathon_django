from django.urls import path
from . import views

urlpatterns =[
   path('',views.index, name='index'),
   path('add_venue', views.add_venue, name='add-venue'),
   path('list_venues', views.list_venues, name="list-venues"),
   path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
   path('search_venues', views.search_venues, name='search-venues'),
   path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
   path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
   path('add_event', views.add_event, name='add-event'),
   path('list_events', views.list_events, name="list-events"),
   path('show_event/<event_id>', views.show_event, name='show-event'),
   path('search_events', views.search_events, name='search-events'),
   path('update_event/<event_id>', views.update_event, name='update-event'),
   path('delete_event/<event_id>', views.delete_event, name='delete-event'),
   path('attend_event/<event_id>', views.attend_event, name='attend-event'),
   path('cancel_attendance/<event_id>', views.cancel_attendance, name="cancel-attendance"),
]