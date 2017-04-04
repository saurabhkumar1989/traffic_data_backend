from django.contrib import admin

# Register your models here.

from .models import Tweets

admin.site.register(Tweets)
