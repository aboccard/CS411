from django.http import HttpResponseRedirect
from django.shortcuts import render
import json

# Create your views here.

from .forms import RestaurantForm

from .functions import YELP_GET

def API_caller(request):

	if request.method == "POST":
		form = RestaurantForm(request.POST)

		if form.is_valid():

			YELP_GET(form.cleaned_data)

			form = RestaurantForm()

	else:
		form = RestaurantForm()

	return render(request, 'API_caller.html', {'form': form})