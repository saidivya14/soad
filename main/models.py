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
    price = models.DecimalField(max_digits=10, decimal_places=2)
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
    organisation=models.CharField(max_length=300)
    instructor=models.CharField(max_length=300)
    noofweeks=models.IntegerField()
    video1 = models.FileField(blank='True',upload_to='items/')
    d1=models.CharField(max_length=1000,default='video1')
    
    video2=models.FileField(blank='True',upload_to='items/')
    d2=models.CharField(max_length=1000,default='video2')
    
    video3=models.FileField(blank='True',upload_to='items/')
    d3=models.CharField(max_length=1000,default='video3')
    
    video4=models.FileField(blank='True',upload_to='items/')
    d4=models.CharField(max_length=1000,default='video4')
    
    video5=models.FileField(blank='True',upload_to='items/')
    d5=models.CharField(max_length=1000,default='video5')
    
    
class EnrolledStudents(models.Model):
    
    courseid=models.IntegerField()
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    c1=models.BooleanField(default=False)
    c2=models.BooleanField(default=False)
    c3=models.BooleanField(default=False)
    c4=models.BooleanField(default=False)
    c5=models.BooleanField(default=False)
    
    
    

class CourseStudents(models.Model):

    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    
    created =  models.DateTimeField(auto_now_add=True) 
    v1=models.BooleanField(default=False)
    v2=models.BooleanField(default=False)
    v3=models.BooleanField(default=False)
    v4=models.BooleanField(default=False)
    v5=models.BooleanField(default=False)

    def __str__(self):
        return self.course.title

    def getscore(self):
        score=0
        if self.v1==True:
            score=score+1
        if self.v2==True:
            score=score+1
        if self.v3==True:
            score=score+1
        if self.v4==True:
            score=score+1
        if self.v5==True:
            score=score+1
        return score*20

    def setv1(self):
        self.v1=True
        self.save()
    def setv2(self):
        self.v2=True
        self.save()
    def setv3(self):
        self.v3=True
        self.save()
    def setv4(self):
        self.v4=True
        self.save()
    def setv5(self):
        self.v5=True
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default1.jpg', upload_to='profile_pics')
    About = models.CharField(default='Tell us about your self',max_length=1000)
    skills = models.CharField(default='Add your Skills',max_length=1000)

    def _str_(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Wishlist(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
