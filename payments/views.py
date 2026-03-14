from django.shortcuts import render, redirect
from django.conf import settings
import stripe
from django.urls import reverse

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):

    if request.method == "POST":

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': 'FitHub Premium Access',
                    },
                    'unit_amount': 1500,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('payment_success')),
            cancel_url=request.build_absolute_uri(reverse('checkout')),
        )

        return redirect(session.url)

    return render(request, "payments/checkout.html")


def payment_success(request):
    return render(request, "payments/success.html")