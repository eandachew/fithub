from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import WorkoutPlan
from profiles.models import UserProfile

# Create your views here.

def workout_list(request):
    workouts = WorkoutPlan.objects.all()

    context = {
        'workouts': workouts
    }

    return render(request, 'workouts/workout_list.html', context)


def workout_detail(request, workout_id):

    workout = get_object_or_404(WorkoutPlan, id=workout_id)

    if workout.is_premium:

        if not request.user.is_authenticated:
            messages.warning(request, "Please login to access premium workouts.")
            return redirect('account_login')

        profile, created = UserProfile.objects.get_or_create(user=request.user)

        if not profile.is_premium:
            messages.warning(request, "You must purchase premium access.")
            return redirect('checkout')

    context = {
        'workout': workout
    }

    return render(request, 'workouts/workout_detail.html', context)