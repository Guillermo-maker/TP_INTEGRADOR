from django.shortcuts import render
from .models import *
from .forms import ChoferForm
import datetime
    


def reporte(request):
    
    
    
    
    
    
    
    
    
    data = Viaje.objects.all()
    dataFiltrada = Viaje.objects.all().filter(dia=datetime.date.today())
    promedio_previ2 = 0
    promedio2 = 0
    toPage = []
    for i in data:
        
        toMinutes = ((i.hora_inicio_prevista.hour) * 60) + i.hora_inicio_prevista.minute
        toMinutes -= ((i.hora_fin.hour) * 60) + i.hora_fin.minute
        
        toMinutes2 = ((i.hora_inicio.hour) * 60) + i.hora_inicio.minute
        toMinutes2 -= ((i.hora_fin.hour) * 60) + i.hora_fin.minute
        
        diferencia = toMinutes - toMinutes2
        
        
        
        toPage.append({'nViaje': i.recorrido.nombre, 'dmViaje':toMinutes, 'dmViaje2':toMinutes2, 'demora':diferencia, })
  
    

