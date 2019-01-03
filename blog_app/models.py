from django.db import models

# Create your models here.

from django.conf import settings
from django.utils import timezone

# use "python manage.py makemigrations blog_app" cmd after a model is created / modified
# this will migrate the change to our database

class Post(models.Model):
	"""docstring for Post"""
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	# def __init__(self, arg):
	# 	super(Post, self).__init__()
	# 	self.arg = arg

