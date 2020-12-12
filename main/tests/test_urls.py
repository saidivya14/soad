from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *

class TestUrls(SimpleTestCase):
    def test_about_url_is_resolved(self):
        url= reverse('about')
        self.assertEquals(resolve(url).func,about)
    
    def test_login_url_is_resolved(self):
        url= reverse('login')
        self.assertEquals(resolve(url).func,Login)
    
    def test_logout_url_is_resolved(self):
        url= reverse('logout')
        self.assertEquals(resolve(url).func,logout_view)

    def test_register_url_is_resolved(self):
        url= reverse('register')
        self.assertEquals(resolve(url).func,register)

    def test_contact_url_is_resolved(self):
        url= reverse('contact')
        self.assertEquals(resolve(url).func,contact)

    def test_success_url_is_resolved(self):
        url= reverse('success')
        self.assertEquals(resolve(url).func,successMsg)
    
    def test_tracking_url_is_resolved(self):
        url= reverse('tracking')
        self.assertEquals(resolve(url).func,tracking)
    
    def test_certi_url_is_resolved(self):
        url = reverse('certi',kwargs={'id': 1})
        self.assertEquals(resolve(url).func, certi)

    def test_stripecheck_url_is_resolved(self):
        url = reverse('stripecheck',kwargs={'id': 1})
        self.assertEquals(resolve(url).func, stripecheck)

    def test_charge_url_is_resolved(self):
        url = reverse('charge',kwargs={'id': 1})
        self.assertEquals(resolve(url).func, charge)

    