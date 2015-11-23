from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from foodoffers.models import *

from forms import NewUser, Offer

def populate_home_page(request):
    return render(request, 'index.html', {})

def populate_browse(request):
    return render(request, 'browse.html', {'offer_list': FoodOffer.objects.all()})

def populate_long_offer(request, offer_id):
    offer_id = int(offer_id)
    try:
        offer = FoodOffer.objects.get(pk=offer_id)
    except:
        raise Http404("Offer " + str(offer_id) + " does not exist.")
        
    return render(request, 'long_offer.html', {'offer': offer})

def get_new_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewUser(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewUser()

    return render(request, 'new_user.html', {'form': form})
    
def populate_user_created(request):
    return render(request, 'user_created.html', {})

def get_new_offer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Offer(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Offer()

    return render(request, 'name.html', {'form': form})