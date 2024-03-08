from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from datetime import date

class Venue(models.Model):
	name = models.CharField('Venue Name', max_length=200)
	address = models.CharField(max_length=500)
	postcode = models.CharField('Postcode', max_length=50)
	phone = models.CharField('Contact Phone', max_length=50, blank=True)
	web = models.URLField('Website Address', blank=True)
	email_address = models.EmailField('Email Address', blank=True)
	owner = models.IntegerField('Venue Owner', blank=False, default=1)
	venue_image =  CloudinaryField('image', default='placeholder')

	def __str__(self):
		return self.name


class Events(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')

class Event(models.Model):
	name = models.CharField('Event Name', max_length=200)
	event_date = models.DateTimeField('Event Date')
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='managed_events')
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(User, related_name='attendees', blank=True)
	max_attendees = models.PositiveIntegerField('Maximum Attendees', default=0)
	event_image =  CloudinaryField('image', default='placeholder')

	def __str__(self):
		return self.name

	@property
	def Days_till(self):
		today = date.today()
		days_till = self.event_date.date() - today
		days_till_stripped = str(days_till).split(",", 1)[0]
		return days_till_stripped
	
	@property
	def Is_Past(self):
		today = date.today()
		if self.event_date.date() < today:
			thing = "Past"
		else:
			thing = "Future"
		return thing

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
		

class Comment(models.Model):
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.review}"
	