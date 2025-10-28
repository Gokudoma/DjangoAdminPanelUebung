from django.contrib import admin
from .models import Booking 

class BookingAdmin(admin.ModelAdmin):
    list_filter = ('confirmed',) 
    
admin.site.register(Booking, BookingAdmin)