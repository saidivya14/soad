from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='blog-home'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path('contact', views.contact,name='contact'),
    path('about',views.about,name='about'),
    url(r'^results/$',views.search,name='search'),
]
