from django.shortcuts import render

# Create your views here.

def API_caller(request):
	return render(request, 'API_caller.html', {})