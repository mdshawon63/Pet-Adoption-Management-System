from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = [
        ("User", "User"),
        ("Admin", "Admin"),
    ]

    phone = models.CharField(
        max_length=20,
        blank=True
    )
    location = models.CharField(
        max_length=100,
        blank=True
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="User"
    )
    
    def __str__(self):
        return self.username