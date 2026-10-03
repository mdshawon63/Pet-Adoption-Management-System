from django.urls import path

from .web_views import (
    home,
    pet_list,
    pet_detail,
)


urlpatterns = [

    path(
        "",
        home,
        name="home"
    ),

    path(
        "pets/",
        pet_list,
        name="pet_list"
    ),

    path(
        "pets/<int:pk>/",
        pet_detail,
        name="pet_detail"
    ),
]