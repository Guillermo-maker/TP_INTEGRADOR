from django.shortcuts import render
from .models import *
    

def lal(request):
   viajes = Viaje.objects.all()
   
   viajesAnalisis= Viaje.objects
   
   
   return render(request,'administracion/ejemplo.html',{"viajes":viajes})

