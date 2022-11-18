from django.contrib import admin

from .models import *

class BusAdmin(admin.ModelAdmin):
    list_filter = ("patente","numero_unidad")
    search_fields = ['patente']

class ChoferAdmin(admin.ModelAdmin):
    list_filter = ("legajo","nombre","apellido")
    search_fields = ['nombre','apellido']
    
class AtractivoAdmin(admin.ModelAdmin):
    list_filter = ("nombre","calificacion",)
    search_fields = ['nombre',"calificacion"]

    
    
class DetalleCadaParadaAdmin(admin.ModelAdmin):
    list_filter = ("numero_orden","conexion","parada")
    search_fields = ['numero_orden']
    
    
class ParadaAdmin(admin.ModelAdmin):
    list_filter = ("nombre","direccion","atractivos")
    search_fields = ['nombre']
    
    
class RecorridoAdmin(admin.ModelAdmin):
    list_filter = ("nombre","frecuencia",'duracion_aprox')
    search_fields = ['nombre']
    
    
class ViajeAdmin(admin.ModelAdmin):
    list_filter = ("hora_inicio_prevista","numero","hora_fin")
    search_fields = ['numero']

admin.site.register(Bus,BusAdmin)
admin.site.register(Chofer,ChoferAdmin)
admin.site.register(Atractivo,AtractivoAdmin)
admin.site.register(DetalleCadaParada,DetalleCadaParadaAdmin)
admin.site.register(Parada,ParadaAdmin)
admin.site.register(Recorrido,RecorridoAdmin)
admin.site.register(Viaje,ViajeAdmin)
