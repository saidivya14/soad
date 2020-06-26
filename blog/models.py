from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self,*args,**kwargs):
        super().save()

        img=Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Post(models.Model):
    CATEGORY = (
        ('Paintings', 'Paintings'),
        ('Historic', 'Historic'),
        ('Others', 'Others'),
    )
    title= models.CharField(max_length=300, unique=True)
    minprice= models.FloatField()
    image=models.ImageField(blank='True',upload_to='items/')
    category=models.CharField(max_length=300, choices=CATEGORY)
    description= models.TextField()
    author=models.CharField(max_length=300,default='username')


    



    

    
   
    
   
