from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import logout
from main.models import Product,Wishlist
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
import requests
from requests.exceptions import RequestException
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm

# Create your views here.
def home(request):
	return render(request,'main/home.html')

def tracking(request):
	return render(request,'main/tracking.html')

def add_to_wishlist(request,id):
    product = Product.objects.get(pk=id)
    ws = Wishlist.objects.filter(product=product).filter(username=request.user)
    if ws:
        posts = Wishlist.objects.filter(username=request.user)
    else:
        Wishlist.objects.create(product=product,username=request.user)
        posts = Wishlist.objects.filter(username=request.user)
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context={
        'posts' : posts
    }
    return render(request,'main/my_wishlist.html',context)

def delete_from_wishlist(request,id):
    product = Product.objects.get(pk=id)
    ws = Wishlist.objects.filter(product=product).filter(username=request.user)
    ws.delete()
    posts = Wishlist.objects.filter(username=request.user)
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context={
        'posts' : posts
    }
    return render(request,'main/my_wishlist.html',context)


def single_product(request,id):
    products = Product.objects.get(pk=id)
    cart_product_form = CartAddProductForm()
    ws = Wishlist.objects.filter(product=products).filter(username=request.user)
    if ws:
        return render(request,'main/single_product1.html', {'products':products,'cart_product_form':cart_product_form})
    else:
        return render(request,'main/single_product.html', {'products':products,'cart_product_form':cart_product_form})

def contact(request):
	return render(request,'main/contact.html')
	
def about(request):
	return render(request,'main/about.html')

def get_courses():
    try:
        ads = requests.get("http://localhost:8000/api/courses")
        return ads.json()
    except RequestException:
        print("Ad server not running/connecting")
        return {}

def coursepage(request):
    asetrack = {}
    asetrack['advts'] = get_courses()
    return render(request, "main/course.html", asetrack)

def get_products():
    try:
        ads = requests.get("http://localhost:8000/api/products")
        return ads.json()
    except RequestException:
        print("Ad server not running/connecting")
        return {}

def shop(request):
    asetrack = {}
    itemlist = get_products()
    paginator = Paginator(itemlist,9)
    page = request.GET.get('page')
    itemlist = paginator.get_page(page)
    asetrack['items'] = itemlist
    return render(request, "main/shop.html", asetrack)

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            d = {'username': username}
            subject, from_email, to = 'Welcome', 'rachabhavani955@gmail.com', email
            content = 'Thanks {0} for registering'.format(username)
            msg = EmailMultiAlternatives(subject, content, from_email, [to])
            # msg.attach_alternative(content, "text / html")
            msg.send()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form, 'title': 'Register here'})


def Login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__ 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'Welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

# Create your views here.
@login_required
def profile(request):
	if request.method== 'POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account is updated ')
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)
	context={
		'u_form' :u_form,
		'p_form' :p_form
		
	}
	return render(request,'main/profile.html',context)