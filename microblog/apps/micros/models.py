from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Blog(models.Model):
	title = models.CharField(max_length=45)
	description = models.TextField(max_length=145)
	user_comment = models.ForeignKey(User)

# Create your models here.
