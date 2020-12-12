"""soad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/',include('orders.urls')),
    path('profile/',main_views.profile,name='profile'),
    path('edit_profile/', main_views.edit_profile, name='edit_profile'),
    path('shop', main_views.shop, name="shop"),
    path('mycourses', main_views.mycourses, name="mycourses"),
    path('product/<int:id>', main_views.single_product, name='shopitem'),
    path('coursedetail/<int:id>', main_views.coursedetail, name='coursedetail'),
    path('v1/<int:id>', main_views.video1, name='v1'),
    path('v2/<int:id>', main_views.video2, name='v2'),
    path('v3/<int:id>', main_views.video3, name='v3'),
    path('v4/<int:id>', main_views.video4, name='v4'),
    path('v5/<int:id>', main_views.video5, name='v5'),
    path('p1/<int:cat>', main_views.pricerange1, name='p1'),
    path('p2/<int:cat>', main_views.pricerange2, name='p2'),
    path('p3/<int:cat>', main_views.pricerange3, name='p3'),
    path('s1/', main_views.shop1, name='s1'),
    path('s2/', main_views.shop2, name='s2'),
    path('s3/', main_views.shop3, name='s3'),
    path('courses', main_views.coursepage, name="courses"),
    path('allcourses', main_views.allcoursepage, name="allcourses"),
    path('photography', main_views.photography, name="photography"),
    path('music', main_views.music, name="music"),
    path('paint', main_views.paint, name="paint"),
    path('dance', main_views.dance, name="dance"),
    path('', include('main.urls')),
    path('stripecheck/<int:id>/',main_views.stripecheck,name='stripecheck'),
    path('charge/<int:id>/', main_views.charge, name="charge"),
    path('success', main_views.successMsg, name="success"),
    path('product/<int:id>', main_views.single_product, name='shopitem'),
    path('cart/', include('cart.urls')),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='main/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='main/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='main/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='main/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
