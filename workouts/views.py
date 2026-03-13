from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import WorkoutPlan

# Create your views here.

def workout_list(request):
    workouts = WorkoutPlan.objects.all()

    context = {
        'workouts': workouts
    }

    return render(request, 'workouts/workout_list.html', context)


def workout_detail(request, workout_id):
    workout = get_object_or_404(WorkoutPlan, id=workout_id)

    # Restrict premium workouts
    if workout.is_premium and not request.user.is_authenticated:
        messages.warning(request, "This workout is premium. Please login or subscribe.")
        return redirect('workouts')

    context = {
        'workout': workout
    }

    return render(request, 'workouts/workout_detail.html', context)
