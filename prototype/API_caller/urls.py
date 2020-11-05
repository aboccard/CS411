from django.urls import path
from API_caller import views

urlpatterns = [
    path('', views.API_caller, name='API_caller'),
]