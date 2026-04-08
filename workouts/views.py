from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import WorkoutPlan, Exercise
from profiles.models import UserProfile
from .models import ExerciseProgress
from django.http import JsonResponse

# Create your views here.


def workout_list(request):
    """Display all workout plans"""
    workouts = WorkoutPlan.objects.all()

    context = {"workouts": workouts}

    return render(request, "workouts/workout_list.html", context)


def workout_detail(request, workout_id):
    """View workout details with premium access control"""
    workout = get_object_or_404(WorkoutPlan, id=workout_id)
    completion_percent = 0

    # Check premium access
    has_premium = False
    if request.user.is_authenticated:
        try:
            has_premium = request.user.profile.is_premium
        except UserProfile.DoesNotExist:
            # Create profile if it doesn't exist
            profile = UserProfile.objects.create(user=request.user)
            has_premium = profile.is_premium

    # Handle premium workout access
    if workout.is_premium:
        if not request.user.is_authenticated:
            messages.warning(request, "Please login to access premium workouts.")
            return redirect("account_login")

        if not has_premium:
            messages.warning(
                request, "You must purchase premium access to view this workout."
            )
            return redirect("premium_checkout")

    # Prepare exercise progress dictionary
    exercises = workout.exercises.all()
    progress_dict = {}
    if request.user.is_authenticated:
        progress = ExerciseProgress.objects.filter(
            user=request.user, exercise__in=exercises
        )
        progress_dict = {p.exercise.id: p.completed for p in progress}

        # Calculate percentage
    total_exercises = exercises.count()
    if total_exercises > 0:
        completed_exercises = sum(
            1 for completed in progress_dict.values() if completed
        )
        completion_percent = int((completed_exercises / total_exercises) * 100)

    context = {
        "workout": workout,
        "has_premium": has_premium,
        "progress": progress_dict,
        "completion_percent": completion_percent,
    }

    return render(request, "workouts/workout_detail.html", context)


def update_progress(request):

    if request.method == "POST" and request.user.is_authenticated:

        exercise_id = request.POST.get("exercise_id")
        completed = request.POST.get("completed") == "true"

        exercise = Exercise.objects.get(id=exercise_id)

        progress, created = ExerciseProgress.objects.get_or_create(
            user=request.user, exercise=exercise
        )

        progress.completed = completed
        progress.save()

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"})
