from django.http import HttpResponseRedirect
from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests
import json

# Create your views here.

from .forms import RestaurantForm

load_dotenv()

YELP_KEY = str(os.getenv('YELP_KEY'))


def YELP_GET(input):

	location = input['location']

	url_params = {'location': location }

	url = "https://api.yelp.com/v3/businesses/search"

	headers = {'Authorization': 'Bearer %s' % YELP_KEY,}

	response = requests.request('GET', url, headers=headers, params=url_params)

	print(response.json())



def API_caller(request):

	if request.method == "POST":
		form = RestaurantForm(request.POST)

		if form.is_valid():

			YELP_GET(form.cleaned_data)

			form = RestaurantForm()

	else:
		form = RestaurantForm()

	return render(request, 'API_caller.html', {'form': form})