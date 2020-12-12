from django.test import TestCase, Client
from django.urls import reverse 
from orders.models import Order,OrderItem,OrderUpdate
from orders.views import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_url = reverse('order_create')
        self.sindex_url = reverse('sindex',kwargs={'id':1})
        self.scharge_url = reverse('scharge',kwargs={'id':1})
        #self.ssuccess_url = reverse('ssuccess')

    def test_about_GET(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)

    
    
    
