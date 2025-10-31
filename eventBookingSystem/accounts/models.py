from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('organizer', 'Organizer'),
    ]

    username = models.CharField(max_length=50, unique=False)
    email = models.EmailField(max_length=30,unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','role']

    def __str__(self):
        return f'{self.username} ({self.email}) - {self.role}'
