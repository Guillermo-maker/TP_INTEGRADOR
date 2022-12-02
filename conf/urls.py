from django.contrib import admin
from django.urls import path
from administracion.views import reporte

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reporte/', reporte),
    
]

