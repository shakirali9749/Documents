from django.contrib import admin

from .models import Event, Ticket

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','category','location','organizer','price','availabe_seats','start_time','end_time')
    search_fields = ('title','location')
    list_filter = ('title',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('event','ticket_type','price','quantity','remaining_quantity')
    search_fields = ('ticket_type','event_title')