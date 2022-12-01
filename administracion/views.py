from django.shortcuts import render
from .models import *
    

def lal(request):
   viajes = Viaje.objects.all()
   return render(request,'administracion/ejemplo.html',{"viajes":viajes})


def reporte(request):
    data = Viaje.objects.all()
    return render(request, 'administracion/reporte.html',{'data': data})


def login(request):
    chofer = Chofer.objects.all()
    return render(request, 'administracion/login.html',{'chofer': chofer})


    """FERCHOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    
    """
















def data_read_buses(request):
    context ={'data_read_chofer':Bus.objects.all()}
    return render (request, "data_read_chofer.html",context)