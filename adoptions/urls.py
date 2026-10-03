from django.urls import path

from .views import (
    AdoptionRequestListCreateAPIView,
    AdoptionRequestDetailAPIView,
)


urlpatterns = [

    path(
        "",
        AdoptionRequestListCreateAPIView.as_view(),
        name="adoption-list-create"
    ),

    path(
        "<int:pk>/",
        AdoptionRequestDetailAPIView.as_view(),
        name="adoption-detail"
    ),
]