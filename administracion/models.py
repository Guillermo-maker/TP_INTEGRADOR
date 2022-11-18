from django.db import models


# Create your models here.

class Bus(models.Model):
    patente = models.IntegerField(blank=True, null=True)  
    numero_unidad = models.IntegerField(blank=True, null=True) 
    fecha_compra = models.DateField(blank=True, null=True) 
    estado = models.BooleanField(blank=True, null=True)  
    
    def __str__(self) -> str:
        return f"-N de patente: {self.patente} -Estado: {self.estado} -N de unidad: {self.numero_unidad}"

    
  
class Chofer(models.Model):
    legajo = models.CharField(max_length=50, blank=True, null=True)
    nombre= models.CharField(max_length=50, blank=True, null=True) 
    apellido = models.CharField(max_length=50, blank=True, null=True) 

def __str__(self) -> str:
        return f"-Legajo: {self.legajo} -Nombre: {self.nombre} -Apellido: {self.apellido}"


class Atractivo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)  
    calificacion = models.FloatField(blank=True, null=True)  
    

class Parada(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)  
    descripcion = models.TextField(blank=True, null=True) 
    direccion = models.CharField(max_length=50, blank=True, null=True) 
    foto = models.CharField(max_length=50, blank=True, null=True)  
    atractivos = models.ManyToManyField(Atractivo)
    
class DetalleCadaParada(models.Model):
    numero_orden = models.IntegerField(blank=True, null=True) 
    conexion = models.IntegerField(blank=True, null=True)  
    parada = models.ForeignKey(Parada, models.DO_NOTHING, blank=True, null=True)  
        

class Recorrido(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True) 
    hora_inicio = models.DateTimeField(blank=True, null=True) 
    hora_finalizacion = models.DateTimeField(blank=True, null=True)  
    duracion_aprox = models.IntegerField(blank=True, null=True)  
    frecuencia = models.PositiveIntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)  
    lista_detalle_parada = models.ForeignKey(DetalleCadaParada, models.DO_NOTHING,blank=True, null=True)  
   
class Viaje(models.Model):
    hora_inicio_prevista = models.DateTimeField(blank=True, null=True)  
    hora_inicio = models.DateTimeField(blank=True, null=True)  
    hora_fin = models.DateTimeField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bus = models.ForeignKey(Bus, models.DO_NOTHING, blank=True, null=True)
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING, blank=True, null=True)
    recorrido = models.ForeignKey(Recorrido, models.DO_NOTHING, blank=True, null=True)
        





        
        




