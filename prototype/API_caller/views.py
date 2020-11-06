from django.http import HttpResponseRedirect
from django.shortcuts import render
import json

# Create your views here.

from .forms import LocationForm

from .functions import YELP_GET

def API_caller(request):

	if request.method == "POST":
		form = LocationForm(request.POST)

		if form.is_valid():

			location = form.cleaned_data['location']

			results = YELP_GET(location)

			return render(request, 'results.html', {'location': location, 'results': results})


	form = LocationForm()

	return render(request, 'API_caller.html', {'form': form})