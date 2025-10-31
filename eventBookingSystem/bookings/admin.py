from django.contrib import admin

from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer','event','ticket','quantity','total_price','is_confirmed','booking_date')
    search_fields = ('cusomer_username', 'event_title')
    list_filter = ('is_confirmed','event')