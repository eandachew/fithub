from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Product, Order, OrderItem

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
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    
    request.session['cart'] = cart
    messages.success(request, "Product added to cart")
    return redirect('products')

def update_cart(request, product_id):
    """Update quantity of a product in cart"""
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        product_id = str(product_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity <= 0:
            # Remove item if quantity is 0 or less
            if product_id in cart:
                del cart[product_id]
        else:
            # Update quantity
            cart[product_id] = quantity
        
        request.session['cart'] = cart
        
        # Calculate new total for this product and overall cart
        product = get_object_or_404(Product, id=product_id)
        total_price = product.price * quantity
        
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
                'cart_total': f"{cart_total:.2f}"
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