from django.db import models


class Site(models.Model):
	sitename = models.CharField(max_length=41)
	description = models.CharField(max_length=41)
	about = models.TextField(max_length=400)
	url = models.URLField(null=True, blank=True)

	sourcecode = models.URLField(null=True, blank=True)
	backend = models.CharField(max_length=150)	
	frontend = models.CharField(max_length=150)	
	responsive = models.BooleanField()
	highlight = models.BooleanField()

	thumbnail = models.ImageField(upload_to='screenshots/')
	image1_description = models.CharField(max_length=40)
	image1 = models.ImageField(upload_to='screenshots/')
	image2_description = models.CharField(max_length=40)
	image2 = models.ImageField(upload_to='screenshots/')
	image3_description = models.CharField(max_length=40, blank=True)
	image3 = models.ImageField(upload_to='screenshots/', null=True, blank=True)
	image4_description = models.CharField(max_length=40, blank=True)
	image4 = models.ImageField(upload_to='screenshots/', null=True, blank=True)

	def __str__(self):
		return self.sitename


class Contact(models.Model):
	navn = models.CharField(max_length=100)
	email = models.EmailField()
	besked = models.TextField(max_length=10000)

	def __str__(self):
		return f'{self.navn} | {self.besked}'