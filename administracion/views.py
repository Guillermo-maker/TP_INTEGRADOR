from django.shortcuts import render,redirect, get_object_or_404
from .models import Recorrido,Bus,Chofer,Atractivo, Viaje
from .forms import BusForm,ChoferForm,AtractivoForm


def home(request):
    recorridos = Recorrido.objects.all()
    return render(request,'home.html',{'recorridos':recorridos})


def data_read_buses(request):
    context ={'data_read_buses':Bus.objects.all()}
    return render (request, "data_read_buses.html",context)


def data_form_buses (request):
    if request.method == "POST":
        form = BusForm (request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/listabus')
    else:
        form = BusForm ()
        return render (request, "data_form_buses.html",{'form':form})     


def data_read_choferes(request):
    context ={'data_read_choferes':Chofer.objects.all()}
    return render (request, "data_read_choferes.html",context)


def data_form_choferes(request):
    if request.method == "POST":
        form = ChoferForm (request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/listachofer')
    else:
        form = ChoferForm ()
        return render (request, "data_form_choferes.html",{'form':form})        


def data_read_atractivos(request):
    context ={'data_read_atractivos':Atractivo.objects.all()}
    return render (request, "data_read_atractivos.html",context)


def data_form_atractivos(request):
    if request.method == "POST":
        form = AtractivoForm (request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/listaatractivo')
    else:
        form = AtractivoForm ()
        return render (request, "data_form_atractivos.html",{'form':form})  

def eliminarAtractivo(request, nombre):
    atractivo = Atractivo.objects.get(nombre=nombre)
    atractivo.delete()
    return redirect ('/listaatractivo')






def renderViajes(request):
    total_viajes = Viaje.objects.count()
    viajes = Viaje.objects.order_by("-hora_inicio_prevista")
    return render(request, "viajes.html", {"viajes": viajes, "total_viajes": total_viajes})


def viajes_detail(request, post_id):
    viaje = get_object_or_404(Viaje, pk=post_id)
    return render(request, "viajes_detail.html", {"viaje": viaje})