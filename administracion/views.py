from django.shortcuts import render
from .models import Recorrido

def home(request):
    recorridos = Recorrido.objects.all()
    return render(request,'home.html',{'recorridos':recorridos})
