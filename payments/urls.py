from django.urls import path
from . import views

urlpatterns = [
    # Shop payment URLs
    path("shop/checkout/", views.shop_checkout, name="shop_checkout"),
    path("shop/success/", views.shop_success, name="shop_success"),
    # Premium payment URLs
    path("premium/checkout/", views.premium_checkout, name="premium_checkout"),
    path("premium/success/", views.premium_success, name="premium_success"),
]
