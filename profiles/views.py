from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import Order

# Create your views here.

@login_required
def profile(request):

    orders = Order.objects.filter(user=request.user)

    context = {
        "orders": orders
    }

    return render(request, "profiles/profile.html", context)