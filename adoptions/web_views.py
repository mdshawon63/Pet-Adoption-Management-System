from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render

from pets.models import Pet

from .forms import AdoptionRequestForm
from .models import AdoptionRequest


@login_required
def adoption_apply(request, pet_id):

    pet = get_object_or_404(Pet, id=pet_id)

    # Check pet status
    if pet.status == "Adopted":
        messages.error(
            request,
            "Sorry, this pet has already been adopted."
        )
        return redirect("pet_detail", pk=pet.id)

    # Check duplicate active request
    existing_request = AdoptionRequest.objects.filter(
        user=request.user,
        pet=pet,
        status__in=["Pending", "Approved"]
    ).exists()

    if existing_request:
        messages.warning(
            request,
            "You already have an active adoption request for this pet."
        )
        return redirect("adoption_dashboard")

    if request.method == "POST":

        form = AdoptionRequestForm(request.POST)

        if form.is_valid():

            adoption_request = form.save(commit=False)

            adoption_request.user = request.user
            adoption_request.pet = pet

            try:
                adoption_request.save()

                messages.success(
                    request,
                    "Your adoption request has been submitted successfully."
                )

                return redirect("adoption_dashboard")

            except ValidationError as e:

                messages.error(
                    request,
                    e.messages[0]
                )

    else:
        form = AdoptionRequestForm()

    return render(
        request,
        "adoptions/adoption_form.html",
        {
            "form": form,
            "pet": pet,
        }
    )


@login_required
def adoption_dashboard(request):

    adoption_requests = AdoptionRequest.objects.filter(
        user=request.user
    ).select_related("pet")

    return render(
        request,
        "adoptions/dashboard.html",
        {
            "adoption_requests": adoption_requests
        }
    )