from django.contrib import admin
from .models import Profile,Product,Course,Wishlist

# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Product)
admin.site.register(Wishlist)