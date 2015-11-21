from django.db import models
import django.contrib.auth.models as authmodels
from django.contrib.localflavor import us

# Create your models here.

class User(authmodels.User):
    zip_code = us.forms.USZipCodeField()
    prof_pic = models.ImageField(upload_to='/profiles/')

class FoodOffer(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now=True)
    address = models.TextField(max_length=1000)
    description = models.TextField(max_length=2000)
    picture = models.ImageField(upload_to='/food/')
    price = models.DecimalField(max_digits=5,decimal_places = 2)
    max_people = models.PositiveSmallIntegerField()
    offer_datetime = models.DateTimeField()

class FoodRequest(models.Model):
    offer = models.ForeignKey(FoodOffer)
    requester = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)

