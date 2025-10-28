from django.contrib import admin
from .models import EventCategory, Location, Event 

admin.site.register(EventCategory)
admin.site.register(Location)
admin.site.register(Event)
