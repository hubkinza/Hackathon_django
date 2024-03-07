from django.urls import path
from . import views

urlpatterns =[
   path('',views.index, name='index'),
   path('add_venue', views.add_venue, name='add-venue'),
   path('list_venues', views.list_venues, name="list-venues"),
   path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
]