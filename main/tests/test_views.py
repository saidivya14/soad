from django.test import  Client
from django.urls import reverse
import json
from main.views import *
from unittest import TestCase

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.about_url = reverse('about')
        self.search_shop_url = reverse('search_shop')
        #self.successmsg_url = reverse('successMsg')
        self.home_url = reverse('home')
        self.tracking_url = reverse('tracking')
        self.contact_url = reverse('contact')
                                
    
    def test_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)

    
    def test_search_shop_GET(self):
        response = self.client.get(self.search_shop_url)
        self.assertEqual(response.status_code, 200)

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
    

    def test_contact_GET(self):
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)



    

    
    #def test_about_GET(self):
     #   response = self.client.get(self.successmsg_url)
      #  self.assertEqual(response.status_code, 200)
