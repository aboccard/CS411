from django import forms

class LocationForm(forms.Form):
    location1 = forms.CharField(label='location1')
    location2 = forms.CharField(label='location2')
    radius = forms.FloatField(label='radius')
    ratio = forms.FloatField(label='ratio')
    budget = forms.FloatField(label='budget')