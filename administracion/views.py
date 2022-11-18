from django.shortcuts import render
from django.http import HttpResponse
    

def lal(request):
   return render(request,'administracion/ejemplo.html')
