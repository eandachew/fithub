from django.shortcuts import render
from shop.models import Product  

# Create your views here.
"""A view to return the index page """

def index(request):
    
    featured_products = Product.objects.all()[:2]
    
    context = {
        'featured_products': featured_products
    }
    return render(request, "home/index.html", context)