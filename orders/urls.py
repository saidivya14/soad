from django.conf.urls import url
from django.urls import path,include
from .import views

urlpatterns = [
    url(r'^create/$',views.order_create,name='order_create'),
    path('sindex/<int:id>',views.sindex,name='sindex'),
    path('scharge/<int:id>',views.scharge,name='scharge'),
    path('ssuccess/<str:args>/',views.ssuccess,name='ssuccess'),

]