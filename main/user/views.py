from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def user(request):

    return render(request, 'Profile.html')