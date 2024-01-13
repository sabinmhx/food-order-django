# orders/views.py
from django.shortcuts import render, redirect
from .models import FoodItem, Order

def menu(request):
    food_items = FoodItem.objects.all()
    return render(request, 'orders/menu.html', {'food_items': food_items})

def cart(request):
    orders = Order.objects.all()
    return render(request, 'orders/cart.html', {'orders': orders})

def delete_from_cart(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    return redirect('cart')

def add_to_cart(request, food_item_id):
    food_item = FoodItem.objects.get(pk=food_item_id)
    order, created = Order.objects.get_or_create(food_item=food_item)
    order.quantity += 1
    order.save()
    return redirect('cart')

def place_order(request):
    Order.objects.all().delete()
    return render(request, 'orders/order_placed.html')

def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html', {'orders': orders})