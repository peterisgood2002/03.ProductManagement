import django
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index( request):
    password = encrypt('U0654t/6')
    
    return HttpResponse("Hello World:" + password)