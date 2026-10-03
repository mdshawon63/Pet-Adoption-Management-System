from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Q

from pets.models import Pet


class AdoptionRequest(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="adoption_requests"
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="adoption_requests"
    )

    phone = models.CharField(max_length=20)

    address = models.TextField()

    reason = models.TextField()

    previous_pet_experience = models.BooleanField(default=False)

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["user", "pet"],
                condition=Q(status__in=["Pending", "Approved"]),
                name="unique_active_adoption_request"
            )
        ]

        ordering = ["-created_at"]

    def clean(self):

        # Pet already adopted
        if self.pet.status == "Adopted":
            raise ValidationError(
                "This pet has already been adopted."
            )

        # Same user + same pet active request check
        existing_request = AdoptionRequest.objects.filter(
            user=self.user,
            pet=self.pet,
            status__in=["Pending", "Approved"]
        )

        if self.pk:
            existing_request = existing_request.exclude(
                pk=self.pk
            )

        if existing_request.exists():
            raise ValidationError(
                "You already have an active adoption request for this pet."
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        super().save(*args, **kwargs)

        # If approved, pet becomes adopted
        if self.status == "Approved":
            Pet.objects.filter(
                id=self.pet_id
            ).update(
                status="Adopted"
            )

    def __str__(self):
        return f"{self.user.username} - {self.pet.name}"