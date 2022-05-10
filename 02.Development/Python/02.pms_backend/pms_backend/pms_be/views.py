import django
from django.http import HttpResponse
from django.shortcuts import render
import os

#from pms_be.models.e_employee import EEmployee
# Create your views here.
from pms_be.models.e_operator import EComplianceVersion

def index( request):
    EComplianceVersion()
    return HttpResponse("Hello World:")
