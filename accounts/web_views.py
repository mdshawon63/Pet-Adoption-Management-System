from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import User


def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        location = request.POST.get("location")
        date_of_birth = request.POST.get("date_of_birth")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if not username or not password:
            messages.error(
                request,
                "Username and password are required."
            )

            return redirect("register")

        if password != password2:
            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("register")
        
        if len(password) < 8:
            messages.error(
            request,
            "Password must be at least 8 characters long."
            )
        return redirect("register")

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("register")

        if email and User.objects.filter(
            email=email
        ).exists():

            messages.error(
                request,
                "Email already exists."
            )

            return redirect("register")

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            location=location,
            date_of_birth=date_of_birth or None,
            password=password,
        )

        messages.success(
            request,
            "Registration successful. Please login."
        )

        return redirect("login")

    return render(
        request,
        "accounts/register.html"
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                f"Welcome, {user.first_name or user.username}!"
            )

            next_url = request.GET.get("next")

            if next_url:
                return redirect(next_url)

            return redirect("home")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "accounts/login.html"
    )


@login_required
def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out."
    )

    return redirect("home")


@login_required
def profile_view(request):

    user = request.user

    if request.method == "POST":

        user.first_name = request.POST.get(
            "first_name"
        )

        user.last_name = request.POST.get(
            "last_name"
        )

        user.email = request.POST.get(
            "email"
        )

        user.phone = request.POST.get(
            "phone"
        )

        user.location = request.POST.get(
            "location"
        )

        date_of_birth = request.POST.get(
            "date_of_birth"
        )

        user.date_of_birth = (
            date_of_birth or None
        )

        if request.FILES.get("profile_picture"):

            user.profile_picture = request.FILES[
                "profile_picture"
            ]

        user.save()

        messages.success(
            request,
            "Profile updated successfully."
        )

        return redirect("profile")

    return render(
        request,
        "accounts/profile.html",
        {
            "user_profile": user
        }
    )