from django.urls import path, include
from .import views
from django.conf.urls import url

app_name = 'cart'

urlpatterns = [
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart-detail/',views.cart_detail,name='cart_detail'),
    path('remove/<int:id>/',views.cart_remove, name='item_decrement'),
]