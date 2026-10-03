from django.urls import path

from .views import (
    PetListCreateAPIView,
    PetDetailAPIView,
)


urlpatterns = [
    path("", PetListCreateAPIView.as_view(), name="pet-list-create"),
    path("<int:pk>/", PetDetailAPIView.as_view(), name="pet-detail"),
]