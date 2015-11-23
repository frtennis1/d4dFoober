from django import forms
import localflavor.us.forms as lfforms

class NewUser(forms.Form):
    username = forms.CharField(label='Desired username', max_length=30) # make sure to later check that this is new
    first_name = forms.CharField(label='Your first name', max_length=30)
    last_name = forms.CharField(label='Your last name', max_length=30)
    email = forms.EmailField(label='Your e-mail')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())
    confirm = forms.CharField(max_length=32, widget=forms.PasswordInput())
    zip_code = lfforms.USZipCodeField()
    prof_pic = forms.ImageField()

class Offer(forms.Form):
    address = forms.CharField(label='Enter the address at which the food will be served',
                            widget = forms.Textarea)
    description = forms.CharField(label='What type of food are you offering? Be as descriptive as possible!',
                            widget = forms.Textarea)  
                            
    # make sure to default this to a logo of a plate                  
    picture = forms.ImageField()
    
    price = forms.DecimalField(min_value = 0, max_value = 999.99, max_digits=5, decimal_places=2)
    max_people = forms.IntegerField(min_value = 1, max_value = 100)
    offer_datetime = forms.DateTimeField()