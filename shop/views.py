from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import redirect
from django.contrib import messages 

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