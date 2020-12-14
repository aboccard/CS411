from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .forms import LocationForm

from .search import searchBusiness

def search(request):

	if request.method == "POST":

		form = LocationForm(request.POST)

		if form.is_valid():

			location1 = form.cleaned_data['location1']
			location2= form.cleaned_data['location2']
			ratio= form.cleaned_data['ratio'] / 100
			radius= form.cleaned_data['radius'] * 1610
			budget = form.cleaned_data['budget']

			if (budget < 10):
				budgetStr = "1"

			elif (budget < 30):
				budgetStr = "1, 2"

			elif (budget < 60):
				budgetStr = "1, 2, 3"

			else:
				budgetStr = "1, 2, 3, 4"

			results = searchBusiness(location1, location2, ratio = ratio, radius= radius, price = budgetStr)

			resultList = []

			for keys in results:
				resultList.append(keys['name'])

			return render(request, 'results.html', {'results': resultList})


	form = LocationForm()

	return render(request, 'SearchBar.html', {'form': form})