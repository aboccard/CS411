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

			# can we make
			nameList = []
			phoneList=[]
			urlList=[]

			for keys in results:
				nameList.append(keys['name'])

			for keys in results:
				phoneList.append(keys['phone'])

			for keys in results:
				urlList.append(keys['url'])

			return render(request, 'results.html', {'names': nameList, 'phones': phoneList, 'urls': urlList})


	form = LocationForm()

	return render(request, 'Final.html', {'form': form})