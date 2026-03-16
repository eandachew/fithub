from django.shortcuts import render, redirect
from django.conf import settings
import stripe
from django.urls import reverse
from shop.models import Order, OrderItem, Product
from profiles.models import UserProfile


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):

    cart = request.session.get("cart", {})

    if not cart:
        return redirect("products")

    total = 0

    for item_id, quantity in cart.items():
        product = Product.objects.get(id=item_id)
        total += product.price * quantity

    order = Order.objects.create(
        user=request.user,
        total=total
    )

    for item_id, quantity in cart.items():
        product = Product.objects.get(id=item_id)

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )

    request.session["order_id"] = order.id

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': f'FitHub Order {order.id}',
                },
                'unit_amount': int(total * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('payment_success')),
        cancel_url=request.build_absolute_uri(reverse('view_cart')),
    )

    return redirect(session.url)


def payment_success(request):

    order_id = request.session.get("order_id")

    if order_id:
        order = Order.objects.get(id=order_id)
        order.paid = True
        order.save()

        # Grant premium access
        profile = request.user.profile
        profile.is_premium = True
        profile.save()

        # Clear cart
        request.session["cart"] = {}

    return render(request, "payments/success.html")