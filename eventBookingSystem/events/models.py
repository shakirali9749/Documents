from django.db import models
from accounts.models import User

class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events', limit_choices_to={'role':'organizer'})
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255)
    start_time= models.DateTimeField()
    end_time = models.DateTimeField()
    total_seats = models.PositiveIntegerField()
    availabe_seats = models.PositiveIntegerField()
    image = models.ImageField(upload_to='events/',blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_available(self):
        return self.availabe_seats > 0

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    remaining_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ticket_type} - {self.event.title}'





