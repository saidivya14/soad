from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from main.models import Product
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm
from . cart import *

def cart_add(request, id):
    cart = Cart(request)  # create a new cart object passing it the request object 
    product = get_object_or_404(Product, id=id) 
    #product = Product.objects.all.get(pk=pid)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request,id=None):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/cart.html', {'cart': cart})