from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import profile, shop, mycourses, single_product, coursedetail, video1, video2, video3,video4,video5,pricerange1,pricerange2,pricerange3, coursepage, allcoursepage, photography, music,paint,dance,stripecheck,charge,successMsg

class TestUrls(SimpleTestCase):
    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_shop_url_is_resolved(self):
        url = reverse('shop')
        print(resolve(url))
        self.assertEquals(resolve(url).func, shop)

    def test_mycourses_url_is_resolved(self):
        url = reverse('mycourses')
        print(resolve(url))
        self.assertEquals(resolve(url).func, mycourses)

    def test_single_product_url_is_resolved(self):
        url = reverse('shopitem',kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, single_product)

    def test_coursedetails_url_is_resolved(self):
        url = reverse('coursedetail',kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, coursedetail)
    
    def test_v1_url_is_resolved(self):
        url = reverse('v1',kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, video1)
    
    def test_v2_url_is_resolved(self):
        url = reverse('v2',kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, video2)

    def test_v3_url_is_resolved(self):
        url = reverse('v3',kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, video3)
    
    def test_v4_url_is_resolved(self):
        url = reverse('v4',kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, video4)
    
    def test_v5_url_is_resolved(self):
        url = reverse('v5',kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, video5)

    def test_p1_url_is_resolved(self):
        url = reverse('p1',kwargs={'cat': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, pricerange1)

    def test_p2_url_is_resolved(self):
        url = reverse('p2',kwargs={'cat': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, pricerange2)
    
    def test_p3_url_is_resolved(self):
        url = reverse('p3',kwargs={'cat': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, pricerange3)
    
    def test_courses_url_is_resolved(self):
        url = reverse('courses')
        print(resolve(url))
        self.assertEquals(resolve(url).func, coursepage)

    def test_allcourses_url_is_resolved(self):
        url = reverse('allcourses')
        print(resolve(url))
        self.assertEquals(resolve(url).func, allcoursepage)

    def test_photography_url_is_resolved(self):
        url = reverse('photography')
        print(resolve(url))
        self.assertEquals(resolve(url).func, photography)

    def test_paint_url_is_resolved(self):
        url= reverse('paint')
        self.assertEquals(resolve(url).func,paint)
    
    def test_music_url_is_resolved(self):
        url= reverse('music')
        self.assertEquals(resolve(url).func,music)

    def test_dance_url_is_resolved(self):
        url= reverse('dance')
        self.assertEquals(resolve(url).func,dance)

    def test_charge_url_is_resolved(self):
        url = reverse('charge',kwargs={'id': 1})
        self.assertEquals(resolve(url).func, charge)

    def test_stripecheck_url_is_resolved(self):
        url = reverse('stripecheck',kwargs={'id': 1})
        self.assertEquals(resolve(url).func, stripecheck)
    
    def test_success_url_is_resolved(self):
        url= reverse('success')
        self.assertEquals(resolve(url).func,successMsg)

    def test_shopitem_url_is_resolved(self):
        url= reverse('shopitem',kwargs={'id': 1})
        self.assertEquals(resolve(url).func,single_product)
    
    



