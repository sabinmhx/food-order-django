# orders/urls.py
from django.urls import path
from .views import menu, cart, add_to_cart, place_order, orders, delete_from_cart

urlpatterns = [
    path('', menu, name='menu'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:food_item_id>/', add_to_cart, name='add_to_cart'),
    path('place_order/', place_order, name='place_order'),
     path('orders/', orders, name='orders'),
    path('cart/', cart, name='cart'),
    path('delete_from_cart/<int:order_id>/', delete_from_cart, name='delete_from_cart'),
]