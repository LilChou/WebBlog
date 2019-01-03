from django.contrib import admin

# Register your models here.

from .models import Post

admin.site.register(Post)  # make it visible on the admin page 

