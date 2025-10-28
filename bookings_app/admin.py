from django.contrib import admin
from .models import Booking, Participant 

class ParticipantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'full_name': ('first_name', 'last_name')}
    list_display = ('first_name', 'last_name', 'full_name', 'email')

admin.site.register(Participant, ParticipantAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_filter = ('confirmed',) 
    readonly_fields = ('booking_date',)
    fields = ('event', 'participant', 'confirmed', 'booking_date')

admin.site.register(Booking, BookingAdmin)