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

# Create your views here.
def home(request):
	return render(request,'main/home.html')

def tracking(request):
	return render(request,'main/tracking.html')

def single_product(request):
	return render(request,'main/single_product.html')

def contact(request):
	return render(request,'main/contact.html')
	
def about(request):
	return render(request,'main/about.html')

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
