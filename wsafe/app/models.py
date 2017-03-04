from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contacts(models.Model):
	users = models.ManyToManyField(User)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=100)
	number = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name
