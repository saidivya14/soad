from rest_framework import serializers
from main.models import Product,Course
from orders.models import Order,OrderItem,OrderUpdate


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['url','id','title','price','image','category','difficulty','description','organisation','instructor','noofweeks']
        lookup_field = "id"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['url','id','title','price','image','category','description','author']
        lookup_field = "id"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['url','id','first_name','last_name','email','address','postal_code','city']
        lookup_field = "id"

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUpdate
        fields = ['url','update_desc','order','place','logistics_name']
        lookup_field = "id"