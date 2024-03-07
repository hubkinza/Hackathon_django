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
   path('add_event', views.add_event, name='add-event')
]