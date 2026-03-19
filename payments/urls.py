from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.payment_success, name='payment_success'),
    path('premium/checkout/', views.premium_checkout, name='premium_checkout'),
    path('premium/success/', views.premium_success, name='premium_success'),

]