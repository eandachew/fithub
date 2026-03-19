import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from profiles.models import UserProfile

stripe.api_key = settings.STRIPE_SECRET_KEY

# SHOP CHECKOUT (cart purchases)

def checkout(request):

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': 'FitHub Shop Purchase',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('payment_success')),
        cancel_url=request.build_absolute_uri(reverse('view_cart')),
    )

    return redirect(session.url)


def payment_success(request):
    return render(request, "payments/success.html")

# PREMIUM WORKOUT PAYMENT

def premium_checkout(request):

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': 'FitHub Premium Membership',
                },
                'unit_amount': 1999,  # €19.99
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('premium_success')),
        cancel_url=request.build_absolute_uri(reverse('workouts')),
    )

    return redirect(session.url)


def premium_success(request):

    profile = request.user.profile
    profile.is_premium = True
    profile.save()

    return render(request, "payments/premium_success.html")