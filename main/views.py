from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import logout
from main.models import Product,Wishlist,Course,CourseStudents
from orders.models import Order,OrderItem,OrderUpdate
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
import requests
from django.db.models import Q
from requests.exceptions import RequestException
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm
import stripe
from django.urls import reverse
from cart.cart import Cart
stripe.api_key = "sk_test_51HqIOnLC1dFeExGNo52wPrsiZrIqvMfDefLTv1Um1jDodhCZwocdMhybjWAME6BsKnpuQbxhMU1H6dntx4bYbT2k00PsDY29ie"
from django_xhtml2pdf.utils import generate_pdf   

# Create your views here.
def stripecheck(request,id):
    product = Course.objects.get(pk=id)
    context = {'product':product}
    return render(request,'main/stripecheck.html',context)

def charge(request,id):
    product = Course.objects.get(pk=id)
    amount=product.price
    if request.method == 'POST':
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
            description="Course payment"
            )
    CourseStudents.objects.create(course=product,student=request.user)
    return redirect(reverse('success'))
    
def certid(request,id):
    resp = HttpResponse(content_type='application/pdf')
    asetrack = {}
    asetrack['user']=request.user
    asetrack['course'] = Course.objects.get(pk=id)
    result = generate_pdf('main/certid.html', file_object=resp,context=asetrack)
    return result

    return render(request,'main/certi.html',asetrack)

def certi(request,id):
    asetrack = {}
    asetrack['user']=request.user
    asetrack['course'] = Course.objects.get(pk=id)
    return render(request,'main/certi.html',asetrack)

def successMsg(request):
    return render(request, 'main/success.html')

def search_shop(request):
    query=request.GET.get('q2')
    if query:
        posts = Product.objects.all()
        results=posts.filter(Q(title__icontains=query)|Q(category__icontains=query))
    else:
        results=Product.objects.all()
    
    paginator = Paginator(results,6)
    page = request.GET.get('page')
    results = paginator.get_page(page)
    context={
        'items' : results
    }
    return render(request,'main/search_shop.html',context)

def home(request):
    return render(request,'main/home.html')

@login_required
def tracking(request):
    if request.method == 'POST':
        orderid = request.POST['order']
        order = Order.objects.get(pk=orderid)
        ordering = OrderUpdate.objects.filter(order=order).first()
        return render(request,'main/tracking.html',{'ordering':ordering})
    return render(request,'main/tracking.html')

@login_required
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

@login_required
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

@login_required
def mywishlist(request):
    posts = Wishlist.objects.filter(username=request.user)
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context={
        'posts' : posts
    }
    return render(request,'main/my_wishlist.html',context)

@login_required
def myorders(request):
    posts = OrderItem.objects.filter(username=request.user)
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context={
        'posts' : posts
    }
    return render(request,'main/myorders.html',context)

@login_required
def single_product(request,id):
    products = Product.objects.get(pk=id)
    cart_product_form = CartAddProductForm()
    ws = Wishlist.objects.filter(product=products).filter(username=request.user)
    if ws:
        return render(request,'main/single_product1.html', {'products':products,'cart_product_form':cart_product_form})
    else:
        return render(request,'main/single_product.html', {'products':products,'cart_product_form':cart_product_form})

@login_required
def coursedetail(request,id):
    asetrack = {}
    asetrack['course'] = Course.objects.get(pk=id)
    course=Course.objects.get(pk=id)
    asetrack['key']=CourseStudents.objects.filter(course=course,student=request.user)
    key=CourseStudents.objects.filter(course=course,student=request.user)
    if key:
        c= CourseStudents.objects.get(course=course,student=request.user)
    
        asetrack['percentage']=c.getscore()
        score=c.getscore()
    else:
        return render(request,'main/coursedetail.html',asetrack)

    if score==100:
        asetrack['completed']=True
    if c.v1==True:
        asetrack['c1']=True
    if c.v2==True:
        asetrack['c2']=True
    if c.v3==True:
        asetrack['c3']=True
    if c.v4==True:
        asetrack['c4']=True
    if c.v5==True:
        asetrack['c5']=True
      
    return render(request,'main/coursedetail.html',asetrack)

def video1(request,id):
    asetrack = {}
    asetrack['course'] = Course.objects.get(pk=id)
    course=Course.objects.get(pk=id)
    asetrack['key']=CourseStudents.objects.filter(course=course,student=request.user)
    
    c= CourseStudents.objects.get(course=course,student=request.user)
    c.setv1()
    if c.v1==True:
        asetrack['c1']=True
    if c.v2==True:
        asetrack['c2']=True
    if c.v3==True:
        asetrack['c3']=True
    if c.v4==True:
        asetrack['c4']=True
    if c.v5==True:
        asetrack['c5']=True
      
    asetrack['percentage']=c.getscore()
    score=c.getscore()
    if score==100:
        asetrack['completed']=True
    return render(request,'main/coursedetail.html',asetrack)

def video2(request,id):
    asetrack = {}
    asetrack['course'] = Course.objects.get(pk=id)
    course=Course.objects.get(pk=id)
    asetrack['key']=CourseStudents.objects.filter(course=course,student=request.user)
    asetrack['c2']=True
    c= CourseStudents.objects.get(course=course,student=request.user)
    c.setv2()
    if c.v1==True:
        asetrack['c1']=True
    if c.v2==True:
        asetrack['c2']=True
    if c.v3==True:
        asetrack['c3']=True
    if c.v4==True:
        asetrack['c4']=True
    if c.v5==True:
        asetrack['c5']=True
    asetrack['percentage']=c.getscore()
    score=c.getscore()
    if score==100:
        asetrack['completed']=True
    return render(request,'main/coursedetail.html',asetrack)

def video3(request,id):
    asetrack = {}
    asetrack['course'] = Course.objects.get(pk=id)
    course=Course.objects.get(pk=id)
    asetrack['key']=CourseStudents.objects.filter(course=course,student=request.user)
    asetrack['c3']=True
    c= CourseStudents.objects.get(course=course,student=request.user)
    c.setv3()
    if c.v1==True:
        asetrack['c1']=True
    if c.v2==True:
        asetrack['c2']=True
    if c.v3==True:
        asetrack['c3']=True
    if c.v4==True:
        asetrack['c4']=True
    if c.v5==True:
        asetrack['c5']=True
    asetrack['percentage']=c.getscore()
    score=c.getscore()
    if score==100:
        asetrack['completed']=True
    return render(request,'main/coursedetail.html',asetrack)

def video4(request,id):
    asetrack = {}
    asetrack['course'] = Course.objects.get(pk=id)
    course=Course.objects.get(pk=id)
    asetrack['key']=CourseStudents.objects.filter(course=course,student=request.user)
    c= CourseStudents.objects.get(course=course,student=request.user)
    c.setv4()
    if c.v1==True:
        asetrack['c1']=True
    if c.v2==True:
        asetrack['c2']=True
    if c.v3==True:
        asetrack['c3']=True
    if c.v4==True:
        asetrack['c4']=True
    if c.v5==True:
        asetrack['c5']=True
    asetrack['percentage']=c.getscore()
    score=c.getscore()
    if score==100:
        asetrack['completed']=True
    return render(request,'main/coursedetail.html',asetrack)

def video5(request,id):
    asetrack = {}
    asetrack['course'] = Course.objects.get(pk=id)
    course=Course.objects.get(pk=id)
    asetrack['key']=CourseStudents.objects.filter(course=course,student=request.user)
    c= CourseStudents.objects.get(course=course,student=request.user)
    c.setv5()
    if c.v1==True:
        asetrack['c1']=True
    if c.v2==True:
        asetrack['c2']=True
    if c.v3==True:
        asetrack['c3']=True
    if c.v4==True:
        asetrack['c4']=True
    if c.v5==True:
        asetrack['c5']=True
    asetrack['percentage']=c.getscore()
    score=c.getscore()
    if score==100:
        asetrack['completed']=True
    return render(request,'main/coursedetail.html',asetrack)

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

def get_products():
    try:
        ads = requests.get("http://localhost:8000/api/products")
        return ads.json()
    except RequestException:
        print("Ad server not running/connecting")
        return {}

def coursepage(request):
    asetrack = {}
    asetrack['advts'] = get_courses()
    keyValList1 = ['Photography']
    keyValList2 = ['Musical Instruments']
    keyValList3 = ['Dance']
    keyValList4 = ['Painting']
    expectedResult1 = [d for d in get_courses() if d['category'] in keyValList1]
    expectedResult2 = [d for d in get_courses() if d['category'] in keyValList2]
    expectedResult3 = [d for d in get_courses() if d['category'] in keyValList3]
    expectedResult4 = [d for d in get_courses() if d['category'] in keyValList4]
    asetrack['photos'] = expectedResult1
    asetrack['music'] = expectedResult2
    asetrack['dance'] = expectedResult3
    asetrack['paints'] = expectedResult4
    return render(request, "main/course.html", asetrack)

@login_required
def mycourses(request):
    asetrack={}
    courses=CourseStudents.objects.filter(student=request.user)
    
    asetrack['courses']=courses
    return render(request, "main/mycourses.html", asetrack)
    
def allcoursepage(request):
    asetrack = {}
    asetrack['advts'] = get_courses()
    
    return render(request, "main/allcourses.html", asetrack)
def photography(request):
    asetrack = {}
    asetrack['advts'] = get_courses()
    keyValList1 = ['Photography']
    expectedResult1 = [d for d in get_courses() if d['category'] in keyValList1]
    asetrack['photos'] = expectedResult1
    return render(request, "main/photography.html", asetrack)
    
def music(request):
    asetrack = {}
    asetrack['advts'] = get_courses()
    keyValList1 = ['Musical Instruments']
    expectedResult1 = [d for d in get_courses() if d['category'] in keyValList1]
    asetrack['music'] = expectedResult1
    return render(request, "main/music.html", asetrack)

def paint(request):
    asetrack = {}
    asetrack['advts'] = get_courses()
    keyValList1 = ['Painting']
    expectedResult1 = [d for d in get_courses() if d['category'] in keyValList1]
    asetrack['paint'] = expectedResult1
    return render(request, "main/painting.html", asetrack)

def dance(request):
    asetrack = {}
    asetrack['advts'] = get_courses()
    keyValList1 = ['Dance']
    expectedResult1 = [d for d in get_courses() if d['category'] in keyValList1]
    asetrack['dance'] = expectedResult1
    return render(request, "main/dance.html", asetrack)

def pricerange1(request,cat):
    asetrack = {}
    asetrack['advts'] = get_courses()
    keyValList1 = ['Photography']
    keyValList2 = ['Musical Instruments']
    keyValList3 = ['Painting']
    keyValList4 = ['Dance']
    if cat==1:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList1 and d['price']<1000]
    elif cat==2:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList2 and d['price']<1000]
    elif cat==3:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList3 and d['price']<1000]
    elif cat==4:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList4 and d['price']<1000]
    else:
        expectedResult = [d for d in get_courses() if  d['price']<1000]
    asetrack['needed'] = expectedResult
    
    return render(request, "main/price1.html", asetrack)

def pricerange2(request,cat):
    asetrack = {}
    asetrack['advts'] = get_courses()
    keyValList1 = ['Photography']
    keyValList2 = ['Musical Instruments']
    keyValList3 = ['Painting']
    keyValList4 = ['Dance']
    if cat==1:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList1 and d['price']>999 and d['price']<5001]
    elif cat==2:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList2 and d['price']>999 and d['price']<5001]
    elif cat==3:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList3 and d['price']>999 and d['price']<5001]
    elif cat==4:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList4 and d['price']>999 and d['price']<5001]
    else:
        expectedResult = [d for d in get_courses() if  d['price'] >999 and d['price']<5001]
    asetrack['needed'] = expectedResult
    
    return render(request, "main/price2.html", asetrack)

def pricerange3(request,cat):
    asetrack = {}
    asetrack['advts'] = get_courses()
    keyValList1 = ['Photography']
    keyValList2 = ['Musical Instruments']
    keyValList3 = ['Painting']
    keyValList4 = ['Dance']
    if cat==1:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList1 and d['price']>5000]
    elif cat==2:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList2 and d['price']>5000]
    elif cat==3:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList3 and d['price']>5000]
    elif cat==4:
        expectedResult = [d for d in get_courses() if d['category'] in keyValList4 and d['price']>5000]
    else:
        expectedResult = [d for d in get_courses() if  d['price']>5000]
    asetrack['needed'] = expectedResult
    
    return render(request, "main/price3.html", asetrack)

def shop(request):
    asetrack = {}
    itemlist = get_products()
    paginator = Paginator(itemlist,9)
    page = request.GET.get('page')
    itemlist = paginator.get_page(page)
    asetrack['items'] = itemlist
    return render(request, "main/shop.html", asetrack)

def shop1(request):
    asetrack = {}
    itemlist=[d for d in get_products() if int(float(d['price']))<1000 ]
    paginator = Paginator(itemlist,9)
    page = request.GET.get('page')
    itemlist = paginator.get_page(page)
    asetrack['items'] = itemlist
    return render(request, "main/shop.html", asetrack)

def shop2(request):
    asetrack = {}
    itemlist=[d for d in get_products() if int(float(d['price'])) >1000 or int(float(d['price']))<10000 or int(float(d['price'])) ==1000]
    paginator = Paginator(itemlist,9)
    page = request.GET.get('page')
    itemlist = paginator.get_page(page)
    asetrack['items'] = itemlist
    return render(request, "main/shop.html", asetrack)

def shop3(request):
    asetrack = {}
    itemlist=[d for d in get_products() if int(float(d['price'])) >10000 or int(float(d['price'])) == 10000]
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
    return render(request, 'main/profile.html')


def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account is updated ')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'main/edit_profile.html', context)