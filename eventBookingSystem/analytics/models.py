from unicodedata import decimal

from django.db import models

from events.models import Event

class EventAnalytics(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='analytics')
    total_bookings = models.PositiveIntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    views = models.PositiveIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Analytics for {self.event.title}'