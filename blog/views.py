from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,SellForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .forms import UserUpdateForm,ProfileUpdateForm 
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.paginator import Paginator 

def home(request):
	return render(request,'blog/home.html')
def about(request):
	return render(request,'blog/about.html')
def prohome(request):
	return render(request,'blog/home.html')
def contact(request):
	return render(request,'blog/contact.html')
def  register(request):
	if request.method== 'POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your orion account.'
			message = render_to_string('acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':account_activation_token.make_token(user),})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(mail_subject, message, to=[to_email])
			email.send()
			return render(request,'blog/emailverification1.html')			
	else:
		form=UserRegisterForm()

	return render(request,'blog/register.html',{'form':form})
def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
        # return redirect('home')
		return render(request,'blog/emailverification2.html')
	else:
		return HttpResponse('Activation link is invalid!')	
@login_required
def getmyitems(request):
	context={
		'items' : Post.objects.filter(author=request.user.username)
	}
	return render(request,'blog/myitems.html',context)
@login_required 
def shop(request):
	posts = Post.objects.all()
	paginator = Paginator(posts,3)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request,'blog/shop.html',{'posts':posts})	
@login_required
def shop_item(request,pid):
	products = Post.objects.get(pk=pid)
	context={
		'products' : products
	}
	return render(request,'blog/shop1.html',context)
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
	return render(request,'blog/profile.html',context)

@login_required
def get_name(request):
	
	if request.method == 'POST':
		
		form = SellForm(request.POST,request.FILES,author=request.user.username)
        
		if form.is_valid():
			print("in get_name")

			form.save()
			return redirect('blog-home')

	else :

		form=SellForm(author=request.user.username)

	
	return render(request, 'blog/sell.html', {'form': form})
