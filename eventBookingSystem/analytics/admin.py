from django.contrib import admin

from .models import EventAnalytics

@admin.register(EventAnalytics)
class EventAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('event', 'total_bookings', 'total_revenue', 'views', 'last_update')
    search_fields = ('event_title',)