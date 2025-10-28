from django.contrib import admin
from .models import EventCategory, Location, Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'date')
    search_fields = ('title', 'date')
    list_filter = ('category',)
    fieldsets = [
        ('Allgemein', {'fields': ('title', 'category', 'date')}),
        ('Organisation', {'fields': ('location', 'capacity')}),
    ]

    date_hierarchy = 'date'

admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory)
admin.site.register(Location)

