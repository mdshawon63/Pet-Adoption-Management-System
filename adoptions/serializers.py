from rest_framework import serializers

from .models import AdoptionRequest


class AdoptionRequestSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(
        source="user.username"
    )

    class Meta:
        model = AdoptionRequest

        fields = [
            "id",
            "user",
            "pet",
            "phone",
            "address",
            "reason",
            "previous_pet_experience",
            "message",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "status",
            "created_at",
        ]

    def validate_pet(self, pet):

        if pet.status == "Adopted":
            raise serializers.ValidationError(
                "This pet has already been adopted."
            )

        request = self.context.get("request")

        if request and request.user.is_authenticated:

            exists = AdoptionRequest.objects.filter(
                user=request.user,
                pet=pet,
                status__in=["Pending", "Approved"]
            ).exists()

            if exists:
                raise serializers.ValidationError(
                    "You already have an active adoption request for this pet."
                )

        return pet


class AdminAdoptionRequestSerializer(
    serializers.ModelSerializer
):

    user = serializers.ReadOnlyField(
        source="user.username"
    )

    class Meta:

        model = AdoptionRequest

        fields = [
            "id",
            "user",
            "pet",
            "phone",
            "address",
            "reason",
            "previous_pet_experience",
            "message",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "pet",
            "phone",
            "address",
            "reason",
            "previous_pet_experience",
            "message",
            "created_at",
        ]