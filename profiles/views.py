from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Order
from profiles.models import UserProfile
from django.contrib import messages
from .forms import ProfileUpdateForm

# Create your views here.


@login_required
def profile_home(request):
    # Get or create user's profile (this fixes the DoesNotExist error)
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Optional: Show a message if profile was just created
    if created:
        messages.info(request, "Welcome! Your profile has been created.")

    # Get user's orders
    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    context = {"profile": profile, "orders": orders}
    return render(request, "profiles/profile_home.html", context)


@login_required
def edit_profile(request):
    # Get or create profile (this fixes the edit profile too)
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("profile_home")
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, "profiles/edit_profile.html", {"form": form})
