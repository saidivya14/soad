from django.shortcuts import render,redirect
from .models import OrderItem,Order,OrderUpdate
from .forms import OrderCreateForm
from django.urls import reverse
from cart.cart import Cart
from django.views.decorators.csrf import csrf_exempt 
import stripe
from django.contrib.auth.models import User
stripe.api_key = "sk_test_51HqIOnLC1dFeExGNo52wPrsiZrIqvMfDefLTv1Um1jDodhCZwocdMhybjWAME6BsKnpuQbxhMU1H6dntx4bYbT2k00PsDY29ie"
app_name = "orders"
# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'],username=request.user)
            
            cart.clear()
            return render(request,'orders/order/created.html',{'order':order})
    else:
        form = OrderCreateForm()
    return render(request,'orders/order/create.html',{'cart':cart,'form':form})

def sindex(request,id):
    order = Order.objects.get(pk=id)
    return render(request, 'orders/payment_index.html',{'item':order})


def scharge(request,id):
    order = Order.objects.get(pk=id)
    amount= order.get_total_cost()
    if request.method== 'POST':
        print('Data:', request.POST)
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['name'],
            source=request.POST['stripeToken'],
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='inr',
            description="shop Payment"

        )
    OrderUpdate.objects.create(order=order)
    return redirect(reverse('ssuccess', args=[amount]))


def ssuccess(request, args):
    amount = args
    return render(request, 'orders/success.html',{'amount':amount})

