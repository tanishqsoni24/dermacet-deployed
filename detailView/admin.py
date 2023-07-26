from django.contrib import admin
from .models import Contact, Career, LevelManufacturing

# Register your models here.

admin.site.register((Contact, Career, LevelManufacturing))
