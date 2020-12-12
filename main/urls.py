from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
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
    path('mywishlist', views.mywishlist, name='wishlist'),
    path('myorders', views.myorders, name='myorders'),
    path('add_to_wishlist/<int:id>', views.add_to_wishlist, name='add-to-wishlist'),
    path('delete_from_wishlist/<int:id>', views.delete_from_wishlist, name='delete-from-wishlist'),
    path('stripecheck/<int:id>/',views.stripecheck,name='stripecheck'),
    path('charge/<int:id>/', views.charge, name="charge"),
    path('success', views.successMsg, name="success"),
    path('certi/<int:id>/', views.certi, name="certi"),
    path('certid/<int:id>/', views.certid, name="certid"),
    url(r'^results-shop/$',views.search_shop,name='search_shop'),
]
