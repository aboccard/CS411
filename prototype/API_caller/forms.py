from django import forms

class RestaurantForm(forms.Form):
    location = forms.CharField(label='Location:', max_length=100)