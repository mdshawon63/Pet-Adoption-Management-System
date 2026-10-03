from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import AdoptionRequest
from .serializers import AdoptionRequestSerializer, AdminAdoptionRequestSerializer
from accounts.permissions import IsOwnerOrAdmin


class AdoptionRequestListCreateAPIView(
    generics.ListCreateAPIView
):

    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        if user.role == "Admin":
            return AdoptionRequest.objects.all()
        return AdoptionRequest.objects.filter(
            user=user
        )

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )


class AdoptionRequestDetailAPIView(
    generics.RetrieveUpdateAPIView
):

    permission_classes = [
        IsAuthenticated,
        IsOwnerOrAdmin
    ]

    def get_queryset(self):

        user = self.request.user

        if user.role == "Admin":
            return AdoptionRequest.objects.all()

        return AdoptionRequest.objects.filter(
            user=user
        )

    def get_serializer_class(self):

        if self.request.user.role == "Admin":
            return AdminAdoptionRequestSerializer

        return AdoptionRequestSerializer