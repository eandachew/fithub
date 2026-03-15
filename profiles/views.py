from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import Order
from payments.models import UserProfile


# Create your views here.

@login_required
def profile_home(request):

    # Get user's profile
    profile = UserProfile.objects.get(user=request.user)

    # Get user's orders
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    context = {
        "profile": profile,
        "orders": orders
    }
    return render(request, "profiles/profile_home.html", context)