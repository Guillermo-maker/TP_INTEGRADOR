from django.contrib import admin
from django.urls import path
from administracion.views import lal,reporte,login,data_read_buses,data_form_buses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', lal),
    path('reporte/', reporte),
    path('login/', login),
    path('agregar_chofer/', data_form_buses),
    path('leer_chofer/', data_read_buses),
    
]

