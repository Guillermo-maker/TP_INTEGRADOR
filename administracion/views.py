from django.shortcuts import render,redirect
from .models import Recorrido,Bus
from .forms import BusForm
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
