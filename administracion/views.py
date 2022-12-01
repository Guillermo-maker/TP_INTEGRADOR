from django.shortcuts import render,redirect
from .models import *
from .forms import ChoferForm
    

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

def data_form_buses (request):
    if request.method == "POST":
        form = ChoferForm (request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/leer_chofer')
    else:
        form = ChoferForm ()
        return render (request, "data_from_chofer.html",{'form':form})  