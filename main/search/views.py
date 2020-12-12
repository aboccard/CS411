from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .forms import LocationForm

from .search import search

def search(request):
    
    if request.method == "POST":
		form = LocationForm(request.POST)

		if form.is_valid():

			location1 = form.cleaned_data['location1']
            location2= form.cleaned_data['location2']
            ratio= form.cleaned_data['ratio']
            radius= form.cleaned_data['radius']
            budget = form.cleaned_data['budget']

			results = search(location1, location2, ratio = ratio, radius= radius, price = budget)

			return render(request, 'results.html', {'location': location, 'results': results})


	form = LocationForm()

	return render(request, 'SearchBar.html', {'form': form})