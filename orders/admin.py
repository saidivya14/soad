from django.contrib import admin
from .models import Order,OrderItem,OrderUpdate
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Order,OrderAdmin) 
admin.site.register(OrderItem) 
admin.site.register(OrderUpdate) 
