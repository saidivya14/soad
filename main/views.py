from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'main/home.html')

def tracking(request):
	return render(request,'main/tracking.html')

def single_product(request):
	return render(request,'main/single_product.html')

def contact(request):
	return render(request,'main/contact.html')