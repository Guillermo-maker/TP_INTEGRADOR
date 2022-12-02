from django.shortcuts import render,redirect
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
  
   # datetime.date.today
    
    #for i in dataFiltrada:
        
    #    promedio_previ = ((i.hora_inicio_prevista.hour) * 60) + i.hora_inicio_prevista.minute 
    #    promedio_previ2 +=  promedio_previ
        
        
    #    promedio = ((i.hora_inicio.hour) * 60) + i.hora_inicio.minute 
    #    promedio2 +=  promedio
    
    #try:    
    #    promedio_previ2 = [promedio_previ2 / len(dataFiltrada)]
     #   promedio2 = [promedio2 / len(dataFiltrada)]
        
    #except:
    #    ValueError(ZeroDivisionError)
        
    
    return render(request, 'administracion/reporte.html',{'data': toPage, })

#'fase':promedio_previ2, "fa":promedio2