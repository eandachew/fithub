from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('delivery/', views.delivery_form, name='delivery_form'), 
    path('process-delivery/', views.process_delivery, name='process_delivery'),  
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:product_id>/', views.update_cart, name='update_cart'),
]