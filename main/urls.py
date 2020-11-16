from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('tracking',views.tracking,name='tracking'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.Login, name='login'),
    path('register/', views.register, name='register'),
    path('api/', include('main.api.urls')),
]
