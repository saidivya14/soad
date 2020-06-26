from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from blog.models import Post
from django.forms import HiddenInput
from .models import Profile
class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']
class SellForm(forms.ModelForm):
	
	class Meta:
		model=Post
		fields=['title','minprice','image','category','description','author']
		


	def __init__(self, *args, **kwargs):
		self._user = kwargs.pop('author')
		super(SellForm, self).__init__(*args,**kwargs)
		

	def save(self, commit=True):
		inst = super(SellForm, self).save(commit=False)
		inst.author = self._user
		if commit:
			inst.save()
			self.save_m2m()
		return inst

		