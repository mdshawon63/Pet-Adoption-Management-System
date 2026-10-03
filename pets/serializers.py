from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "animal_type",
            "breed",
            "age",
            "gender",
            "location",
            "description",
            "image",
            "status",
            "created_at",
        ]

        read_only_fields = ["id", "created_at"]