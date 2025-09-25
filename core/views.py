from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("Hello, world! This is the core app.")

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def about(request):
    return render(request, 'about.html')
