from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from djongo import models

# Create your models here.
class Product(models.Model):
    CATEGORY = (
        ('Bongodrum', 'Bongodrum'),
        ('Conga', 'Conga'),
        ('Doublebass', 'Doublebass'),
        ('Guitar', 'Guitar'),
        ('Piano', 'Piano'),
        ('Sitar', 'Sitar'),
        ('Snare_drum', 'Snare_drum'),
        ('Trumpet', 'Trumpet'),
        ('Violin', 'Violin'),
    )
    title= models.CharField(max_length=300, unique=True)
    price= models.IntegerField()
    image=models.ImageField(blank='True',upload_to='items/')
    category=models.CharField(max_length=300, choices=CATEGORY)
    description= models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Course(models.Model):
    CATEGORY=(
        ('Musical Instruments', 'Musical Instruments'),
        ('Photography', 'Photography'),
        ('Dance', 'Dance'), 
        ('Painting', 'Painting'),
        ('Decoration', 'Decoration'),
        ('Cooking', 'Cooking'), 
    )
    DIFFICULTY=(
        ('Beginner', 'Beginner'),
        ('Intermidiate', 'Intermediate'),
        ('Advanced', 'Advanced'),   
    )
    title= models.CharField(max_length=300, unique=True)
    price= models.IntegerField()
    image=models.ImageField(blank='True',upload_to='items/')
    category=models.CharField(max_length=300, choices=CATEGORY)
    difficulty=models.CharField(max_length=300, choices=DIFFICULTY)
    description= models.CharField(max_length=1000)
    orgnaisation=models.CharField(max_length=300)
    instructor=models.CharField(max_length=300)
    noofweeks=models.IntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default1.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)