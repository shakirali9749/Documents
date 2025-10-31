from django.db import models
from accounts.models import User
from events.models import Event, Ticket

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', limit_choices_to={'role': 'customer'})
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='bookings')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=True)

    def __str__(self):
        return f'Booking # {self.id} - {self.customer.username} ({self.event.title})'



