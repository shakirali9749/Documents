from django.db import models

from bookings.models import Booking


class Payment(models.Model):

    PAYMENT_STATUS_CHOICES = [
        ('pending','Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=50, default='credit_card')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'payment {self.transaction_id} - {self.status}'

