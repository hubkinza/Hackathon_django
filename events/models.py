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
