from django.db import models


class Pet(models.Model):
    ANIMAL_TYPE_CHOICES = [
        ("Dog", "Dog"),
        ("Cat", "Cat"),
        ("Bird", "Bird"),
        ("Rabbit", "Rabbit"),
        ("Other", "Other"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    STATUS_CHOICES = [
        ("Available", "Available"),
        ("Adopted", "Adopted"),
    ]

    name = models.CharField(max_length=100)
    animal_type = models.CharField(
        max_length=20,
        choices=ANIMAL_TYPE_CHOICES
    )
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to="pets/",
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Available"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
