from django.test import SimpleTestCase
from django.urls import reverse,resolve
from orders.views import order_create, sindex, scharge, ssuccess

class TestUrls(SimpleTestCase):
    def test_order_create_url_is_resolved(self):
        url = reverse('order_create')
        print(resolve(url))
        self.assertEquals(resolve(url).func, order_create)
    
    def test_sindex_url_is_resolved(self):
        url = reverse('sindex',kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, sindex)

    def test_scharge_url_is_resolved(self):
        url = reverse('scharge',kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, scharge)

    def test_ssuccess_url_is_resolved(self):
        url = reverse('ssuccess',kwargs={'args': 'success'})
        print(resolve(url))
        self.assertEquals(resolve(url).func, ssuccess)


