import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from profiles.models import UserProfile
from shop.models import Product, Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY

# SHOP CHECKOUT (cart purchases)
def shop_checkout(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to complete your purchase")
        
        try:
            return redirect('account_login') 
        except:
            try:
                return redirect('login')  
            except:
                return redirect('/accounts/login/')

    # Get cart from session
    cart = request.session.get('cart', {})
    
    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')
    
    # Create line items from cart and calculate total
    line_items = []
    cart_total = 0
    
    for item_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=item_id)
            line_items.append({
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),  # Convert to cents
                },
                'quantity': quantity,
            })
            cart_total += product.price * quantity
        except Product.DoesNotExist:
            continue
    
    if not line_items:
        messages.error(request, "No valid products in cart.")
        return redirect('view_cart')
    
    try:
        # Create order in database BEFORE payment
        order = Order.objects.create(
            user=request.user,
            total=cart_total,
            paid=False
        )
        
        # Create order items
        for item_id, quantity in cart.items():
            product = Product.objects.get(id=item_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )
        
        # Create Stripe session with order ID
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri(
                reverse('shop_success') + f"?order_id={order.id}"
            ),
            cancel_url=request.build_absolute_uri(reverse('view_cart')),
            metadata={
                'order_id': order.id,
                'user_id': request.user.id
            }
        )
        
        # Store order ID in session
        request.session['current_order_id'] = order.id
        
        return redirect(session.url)
        
    except Exception as e:
        messages.error(request, f"Payment error: {str(e)}")
        return redirect('view_cart')

def shop_success(request):
    # Get order ID from URL
    order_id = request.GET.get('order_id')
    
    if order_id:
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            order.paid = True
            order.save()
            messages.success(request, f"Order #{order.id} completed successfully!")
        except Order.DoesNotExist:
            messages.warning(request, "Order not found.")
    
    # Clear the cart after successful payment
    if 'cart' in request.session:
        del request.session['cart']
    if 'current_order_id' in request.session:
        del request.session['current_order_id']
    
    return render(request, "payments/success.html", {
        'payment_type': 'shop'
    })

# PREMIUM WORKOUT PAYMENT
def premium_checkout(request):
    if request.method == 'POST':
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': 'FitHub Premium Membership',
                        },
                        'unit_amount': 1999,  # €19.99 in cents
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(reverse('premium_success')),
                cancel_url=request.build_absolute_uri(reverse('workouts')),
            )
            return redirect(session.url)
        except Exception as e:
            messages.error(request, f"Payment error: {str(e)}")
            return redirect('checkout')
    
    # GET request - show the checkout form
    return render(request, "payments/checkout.html")

def premium_success(request):
    if request.user.is_authenticated:
        # Get or create profile and set premium status
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.is_premium = True
        profile.save()
        messages.success(request, "Congratulations! You are now a premium member!")
    else:
        messages.warning(request, "Please log in to activate your premium status.")
        return redirect('account_login')
    
    return render(request, "payments/success.html", {
        'payment_type': 'premium'
    })