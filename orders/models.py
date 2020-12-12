from django.db import models
from main.models import Product
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return int(float(self.price * self.quantity))

class OrderUpdate(models.Model):
    CATEGORY = (
        ('Packed', 'Packed'),
        ('Shipped', 'Shipped'),
        ('In-Transit', 'In-Transit'),
        ('Out for delivery', 'Out for delivery'),
    )
    update_desc=models.CharField(max_length=300, choices=CATEGORY,default="Packed")
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    update_id= models.AutoField(primary_key=True)
    place = models.CharField(max_length=5000)
    logistics_name = models.CharField(max_length=5000)