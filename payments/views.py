from django.shortcuts import render
from django.conf import settings
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):

    context = {
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY
    }

    return render(request, "payments/checkout.html", context)


def payment_success(request):

    return render(request, "payments/success.html")