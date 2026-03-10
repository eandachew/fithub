from django.shortcuts import render
from .models import WorkoutPlan

# Create your views here.

def workout_list(request):
    workouts = WorkoutPlan.objects.all()

    context = {
        'workouts': workouts
    }

    return render(request, 'workouts/workout_list.html', context)