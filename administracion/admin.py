from django.contrib import admin

from .models import *

class BusAdmin(admin.ModelAdmin):
    list_filter = ("patente","estado")
    search_fields = ['nestado',"patente"]
    

class ChoferAdmin(admin.ModelAdmin):
    list_filter = ("nombre","legajo")
    search_fields = ['nombre']
    
class AtractivoAdmin(admin.ModelAdmin):
    list_filter = ("nombre","calificacion")
    search_fields = ["nombre"]
    
class ParadaAdmin(admin.ModelAdmin):
    list_filter = ("atractivos","direccion")
    search_fields = ["nombre"]
    
    
class DetalleCadaParadaAdmin(admin.ModelAdmin):
    list_filter = ("conexion","parada")
    search_fields = ["numero_orden"]
    
    
class RecorrioAdmin(admin.ModelAdmin):
    list_filter = ("frecuencia","duracion_aprox","color")
    search_fields = ['hora_incion',"finalizacion"]
    

class ViajeAdmin(admin.ModelAdmin):
    list_filter = ("hora_inicio_prevista","hora_fin")
    search_fields = ["numero"]

admin.site.register(Bus,BusAdmin)
admin.site.register(Chofer,ChoferAdmin)
admin.site.register(Atractivo,AtractivoAdmin)
admin.site.register(DetalleCadaParada,DetalleCadaParadaAdmin)
admin.site.register(Parada,ParadaAdmin)
admin.site.register(Recorrido,RecorrioAdmin)
admin.site.register(Viaje,ViajeAdmin)
