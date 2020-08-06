from django.db import models
from datetime import datetime

from django.urls import reverse
# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=120)
	image = models.FileField(null=True, blank=True)
	content = models.TextField(blank=True, null=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True)
	timestamp = models.DateTimeField(blank=True, default=datetime.now)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("face:detail", args=[str(self.id)])
	

