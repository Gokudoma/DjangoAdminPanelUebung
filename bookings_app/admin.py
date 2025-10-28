from django.contrib import admin
from .models import Booking, Participant 

class BookingAdmin(admin.ModelAdmin):
    list_filter = ('confirmed',) 
    readonly_fields = ('booking_date',)
    fields = ('event', 'participant', 'confirmed', 'booking_date')

admin.site.register(Booking, BookingAdmin)
admin.site.register(Participant)