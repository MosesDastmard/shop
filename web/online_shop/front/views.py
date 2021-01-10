from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'front/home.html', {'word': 'My name is Moses'})

def password(request):
    return render(request, 'front/password.html')