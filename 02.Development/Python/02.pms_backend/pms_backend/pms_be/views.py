import django
from django.http import HttpResponse
from django.shortcuts import render
import os 

# Create your views here.
def index( request):
    return HttpResponse("Hello World:")