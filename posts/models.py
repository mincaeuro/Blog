from django.db import models
import os
import uuid
import datetime
from django.utils import timezone


def get_image_path(instance, filename):
	return os.path.join('photos', str(instance.id), filename)

# Create your models here.

class Prispevok(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=300)
	text = models.TextField(max_length=3000)
	pub_date = models.DateTimeField('date published')
	user = models.CharField(max_length=50)
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	hodnotenie = models.CharField(max_length=1)
	def __str__(self):              # __unicode__ on Python 2
        	return self.title
	
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=3)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Kometar(models.Model):
	id = models.AutoField(primary_key=True)
	postRef = models.ForeignKey(Prispevok, blank=False, default=uuid.uuid4)
	text = models.TextField(max_length=3000)
	pub_date = models.DateTimeField('date published')
	user = models.CharField(max_length=50)
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=3)
