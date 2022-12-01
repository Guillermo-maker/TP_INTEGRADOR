from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def lal(request):
   return render(request,'administracion/ejemplo.html')

def login(request):
    chofer = Chofer.objects.all()
    return render(request, 'administracion/login.html',{'chofer': chofer})