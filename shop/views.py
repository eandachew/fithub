from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Product, Order, OrderItem
from profiles.models import Delivery


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)

def add_to_cart(request, product_id):
    # Get the product to check stock
    product = get_object_or_404(Product, id=product_id)
    
    # Get quantity from POST or default to 1
    quantity = int(request.POST.get('quantity', 1))
    
    # Check if enough stock
    if quantity > product.stock:
        messages.error(request, f"Sorry, only {product.stock} units of {product.name} available!")
        return redirect('product_detail', product_id=product_id)
    
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    
    # Check if adding would exceed stock
    current_qty = cart.get(product_id, 0)
    if current_qty + quantity > product.stock:
        messages.error(request, f"Cannot add {quantity} more. Only {product.stock - current_qty} available in stock!")
        return redirect('product_detail', product_id=product_id)
    
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    
    request.session['cart'] = cart
    messages.success(request, f"{quantity} x {product.name} added to cart")
    return redirect('products')

def update_cart(request, product_id):
    """Update quantity of a product in cart"""
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        product_id = str(product_id)
        quantity = int(request.POST.get('quantity', 1))
        
        # Get product to check stock
        product = get_object_or_404(Product, id=product_id)
        
        if quantity <= 0:
            # Remove item if quantity is 0 or less
            if product_id in cart:
                del cart[product_id]
        else:
            # Check if requested quantity exceeds stock
            if quantity > product.stock:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'status': 'error',
                        'message': f'Sorry, only {product.stock} units available!'
                    }, status=400)
                else:
                    messages.error(request, f"Sorry, only {product.stock} units of {product.name} available!")
                    return redirect('view_cart')
            
            # Update quantity
            cart[product_id] = quantity
        
        request.session['cart'] = cart
        
        # Calculate new total for this product and overall cart
        total_price = product.price * quantity if quantity > 0 else 0
        
        # Calculate cart total
        cart_total = 0
        for item_id, qty in cart.items():
            prod = Product.objects.get(id=item_id)
            cart_total += prod.price * qty
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # AJAX response
            return JsonResponse({
                'status': 'success',
                'quantity': quantity,
                'total_price': f"{total_price:.2f}",
                'cart_total': f"{cart_total:.2f}",
                'stock_remaining': product.stock
            })
        else:
            # Regular form submission
            messages.success(request, "Cart updated successfully")
            return redirect('view_cart')
    
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    """Remove a product from cart"""
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        product_id = str(product_id)
        
        if product_id in cart:
            del cart[product_id]
        
        request.session['cart'] = cart
        
        # Calculate cart total
        cart_total = 0
        for item_id, qty in cart.items():
            prod = Product.objects.get(id=item_id)
            cart_total += prod.price * qty
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # AJAX response
            return JsonResponse({
                'status': 'success',
                'cart_empty': len(cart) == 0,
                'cart_total': f"{cart_total:.2f}"
            })
        else:
            # Regular form submission
            messages.success(request, "Item removed from cart")
            return redirect('view_cart')
    
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    
    for item_id, quantity in cart.items():
        product = Product.objects.get(id=item_id)
        product.quantity = quantity
        product.total_price = product.price * quantity
        total += product.total_price
        products.append(product)
    
    context = {
        "products": products,
        "total": total
    }
    
    return render(request, "shop/cart.html", context)

def delivery_form(request):
    """Show delivery form before checkout"""
    cart = request.session.get('cart', {})
    
    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')
    
    cart_items = {}
    cart_total = 0
    
    for item_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=item_id)
            cart_items[item_id] = {
                'name': product.name,
                'quantity': quantity,
                'price': product.price,
            }
            cart_total += product.price * quantity
        except Product.DoesNotExist:
            continue
    
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'shop/delivery_form.html', context)


def process_delivery(request):
    """Save delivery information and proceed to payment"""
    if request.method == 'POST':
        # Save delivery info to session
        request.session['delivery_info'] = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'address_line1': request.POST.get('address_line1'),
            'address_line2': request.POST.get('address_line2', ''),
            'city': request.POST.get('city'),
            'postal_code': request.POST.get('postal_code'),
            'country': request.POST.get('country'),
        }
        
        # If user is logged in, save to database
        if request.user.is_authenticated:
            Delivery.objects.create(
                user=request.user,
                full_name=request.POST.get('full_name'),
                email=request.POST.get('email'),
                phone_number=request.POST.get('phone_number'),
                address_line1=request.POST.get('address_line1'),
                address_line2=request.POST.get('address_line2', ''),
                city=request.POST.get('city'),
                postal_code=request.POST.get('postal_code'),
                country=request.POST.get('country'),
            )
        
        # Redirect to payment
        return redirect('shop_checkout')
    
    return redirect('view_cart')