from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import timedelta, datetime, timezone
from math import ceil
from django.utils import timezone

# Auction duration in minutes
AUCTION_DURATION = 30

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default1.jpg',upload_to='profile_pics')


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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.SET("(deleted)"),
                               blank=True,
                               null=True,
                               related_name="auction_winner",
                               related_query_name="auction_winner")
    final_value = models.IntegerField(blank=True, null=True)

    def resolve(self):
        if self.is_active:
            # If expired
            if self.has_expired():
                # Define winner
                highest_bid = Bid.objects.filter(auction=self).order_by('-amount').order_by('date').first()
                if highest_bid:
                    self.winner = highest_bid.bidder
                    self.final_value = highest_bid.amount
                self.is_active = False
                self.save()

    # Helper function that determines if the auction has expired
    def has_expired(self):
        now = datetime.now(timezone.utc)
        expiration = self.date_added + timedelta(minutes=AUCTION_DURATION)
        if now > expiration:
            return True
        else:
            return False

    # Returns the ceiling of remaining_time in minutes
    @property
    def remaining_minutes(self):
        if self.is_active:
            now = datetime.now(timezone.utc)
            expiration = self.date_added + timedelta(minutes=AUCTION_DURATION)
            minutes_remaining = ceil((expiration - now).total_seconds() / 60)
            return(minutes_remaining)
        else:
            return(0)


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Post, on_delete=models.CASCADE)
    amount = models.IntegerField()
    # is_cancelled = models.BooleanField(default=False)
    date = models.DateTimeField('when the bid was made')   
    



    

    
   
    
   
