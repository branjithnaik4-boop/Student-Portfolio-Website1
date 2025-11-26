from django.urls import path
from django.shortcuts import render

def index(request):
    return render(request,'simple_project.html')

urlpatterns=[ path('', index) ]
