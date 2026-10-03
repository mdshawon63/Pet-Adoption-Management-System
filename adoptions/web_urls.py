from django.urls import path

from .web_views import adoption_apply, adoption_dashboard


urlpatterns = [
    path(
        "apply/<int:pet_id>/",
        adoption_apply,
        name="adoption_apply"
    ),

    path(
        "dashboard/",
        adoption_dashboard,
        name="adoption_dashboard"
    ),
]