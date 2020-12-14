from django import forms

class LocationForm(forms.Form):
    location1 = forms.CharField(label='location1')
    location2 = forms.CharField(label='location2')
    radius = forms.IntegerField(label='radius')
    ratio = forms.IntegerField(label='ratio')
    budget = forms.IntegerField(label='budget')