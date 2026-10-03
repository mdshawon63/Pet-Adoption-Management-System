from django.shortcuts import render, get_object_or_404

from .models import Pet


def home(request):

    pets = Pet.objects.filter(
        status="Available"
    ).order_by("-created_at")[:6]

    return render(
        request,
        "home.html",
        {
            "pets": pets
        }
    )


def pet_list(request):

    pets = Pet.objects.all().order_by("-created_at")

    search = request.GET.get("search", "")
    animal_type = request.GET.get("animal_type", "")
    breed = request.GET.get("breed", "")
    gender = request.GET.get("gender", "")
    location = request.GET.get("location", "")
    status = request.GET.get("status", "")

    if search:
        pets = pets.filter(
            name__icontains=search
        )

    if animal_type:
        pets = pets.filter(
            animal_type__iexact=animal_type
        )

    if breed:
        pets = pets.filter(
            breed__icontains=breed
        )

    if gender:
        pets = pets.filter(
            gender__iexact=gender
        )

    if location:
        pets = pets.filter(
            location__icontains=location
        )

    if status:
        pets = pets.filter(
            status__iexact=status
        )

    return render(
        request,
        "pets/pet_list.html",
        {
            "pets": pets,
            "search": search,
            "animal_type": animal_type,
            "breed": breed,
            "gender": gender,
            "location": location,
            "status": status,
        }
    )


def pet_detail(request, pk):

    pet = get_object_or_404(
        Pet,
        pk=pk
    )

    return render(
        request,
        "pets/pet_detail.html",
        {
            "pet": pet
        }
    )