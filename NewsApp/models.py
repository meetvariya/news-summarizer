from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Location(models.Model):
# 	LOCATION = (
# 		('Anand', 'Anand'),
# 		('Gandhinagar', 'Gandhinagar'),
# 		('Surat', 'Surat'),
# 		('Baroda', 'Baroda'),
# 		('Ahmedabad', 'Ahmedabad'),
# 	)
#
# 	location_name = models.CharField(max_length=200, null=True, choices=LOCATION)
#
# 	def __str__(self):
# 		return self.location_name

class Customer(models.Model):
	# LANGUAGE = (
	# 	('English', 'English'),
	# 	('Hindi', 'Hindi'),
	# 	('Gujarati', 'Gujarati'),
	# )

	LOCATION = (
		('at', 'Austria'),
		('au', 'Australia'),
		('be', 'Belgium'),
		('bg', 'Bulgaria'),
		('ca', 'Canada'),
		('de', 'Germany'),
		('eg', 'Egypt'),
		('fn', 'France'),
		('gr', 'Greece'),
		('in', 'India'),
		('lt', 'Lithuania'),
		('nl', 'Netherlands'),
		('se', 'Sweden'),
		('sg', 'Singapore'),
		('si', 'Slovenia'),
		('ru', 'Russia'),
	)

	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	# language = models.CharField(max_length=200, default='Gujarati', choices=LANGUAGE)
	location = models.CharField(max_length=200, default='in', choices=LOCATION)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	# location = models.ManyToManyField(Location)


	def __str__(self):
		return self.name
