from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def login(request):

    return render(request, 'Home.html')