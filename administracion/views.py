from django.shortcuts import render
from django.http import HttpResponse
from .models import *
    

def lal(request):
   viajes = Viaje.objects.all()
   
   viajesAnalisis= Viaje.objects
   
   
   return render(request,'administracion/ejemplo.html',{"viajes":viajes})

def login(request):
    chofer = Chofer.objects.all()
    return render(request, 'administracion/login.html',{'chofer': chofer})
