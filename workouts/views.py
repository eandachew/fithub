from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import WorkoutPlan
from profiles.models import UserProfile

# Create your views here.

def workout_list(request):
    """Display all workout plans"""
    workouts = WorkoutPlan.objects.all()

    context = {
        'workouts': workouts
    }

    return render(request, 'workouts/workout_list.html', context)


def workout_detail(request, workout_id):
    """View workout details with premium access control"""
    workout = get_object_or_404(WorkoutPlan, id=workout_id)
    
    # Check premium access
    has_premium = False
    if request.user.is_authenticated:
        try:
            has_premium = request.user.profile.is_premium
        except UserProfile.DoesNotExist:
            # Create profile if it doesn't exist
            from profiles.models import UserProfile
            profile = UserProfile.objects.create(user=request.user)
            has_premium = profile.is_premium

    # Handle premium workout access
    if workout.is_premium:
        if not request.user.is_authenticated:
            messages.warning(request, "Please login to access premium workouts.")
            return redirect('account_login')
        
        if not has_premium:
            messages.warning(request, "You must purchase premium access to view this workout.")
            return redirect('premium_checkout')

    context = {
        'workout': workout,
        'has_premium': has_premium,
    }

    return render(request, 'workouts/workout_detail.html', context)