from django.db import models
import django.contrib.auth.models as authmodels
import localflavor.us.models as lfmodels
import os

# Create your models here.


def rename_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = os.path.join(os.getcwd(), 'pics/profiles/%s.%s' % (instance.username, ext))
    return filename
    
class User(authmodels.User):
    zip_code = lfmodels.USZipCodeField()
    prof_pic = models.ImageField(upload_to=rename_file)
    
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

