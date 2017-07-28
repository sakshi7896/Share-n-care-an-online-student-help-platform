from django.contrib import admin
from .models import Profile, Book, Counselling
from .models import Profile
from django.db import models
admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Counselling)
