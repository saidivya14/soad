from rest_framework import serializers
from main.models import Product,Course


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