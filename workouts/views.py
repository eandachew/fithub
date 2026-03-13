from django.shortcuts import render, get_object_or_404
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

    context = {
        'workout': workout
    }

    return render(request, 'workouts/workout_detail.html', context)