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
    
    def __str__(self) -> str:
        return f"-Nombre: {self.nombre} -Calificacion: {self.calificacion}"

class Parada(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)  
    descripcion = models.TextField(blank=True, null=True) 
    direccion = models.CharField(max_length=50, blank=True, null=True) 
    foto = models.CharField(max_length=50, blank=True, null=True)  
    atractivos = models.ManyToManyField(Atractivo)

    def __str__(self) -> str:
        return f"-Nombre: {self.nombre} -Direccion: {self.direccion} -Atractivos: {self.atractivos}"  

class DetalleCadaParada(models.Model):
    numero_orden = models.IntegerField(blank=True, null=True) 
    conexion = models.IntegerField(blank=True, null=True)  
    parada = models.ForeignKey(Parada, models.DO_NOTHING, blank=True, null=True)  

    def __str__(self) -> str:
        return f"-Numero De Orden: {self.numero_orden} -Conexion: {self.conexion} -Parada: {self.parada}"    

class Recorrido(models.Model):
    dia = models.DateField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True) 
    hora_inicio = models.TimeField(blank=True, null=True) 
    hora_finalizacion = models.TimeField(blank=True, null=True)  
    duracion_aprox = models.TimeField(blank=True, null=True)  
    frecuencia = models.TimeField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)  
    lista_detalle_parada = models.ForeignKey(DetalleCadaParada, models.DO_NOTHING,blank=True, null=True) 

    def __str__(self) -> str:
        return f"-Nombre: {self.nombre} -Hora de inicio {self.hora_inicio} -Hora de Finalizacion: {self.hora_finalizacion} -Duracion Aprox: {self.duracion_aprox}"
 
   
class Viaje(models.Model):
    dia = models.DateField(blank = True, null = True)
    hora_inicio_prevista = models.TimeField(blank=True, null=True)  
    hora_inicio = models.TimeField(blank=True, null=True)  
    hora_fin = models.TimeField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bus = models.ForeignKey(Bus, models.DO_NOTHING, blank=True, null=True)
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING, blank=True, null=True)
    recorrido = models.ForeignKey(Recorrido, models.DO_NOTHING, blank=True, null=True)
        
    def __str__(self) -> str:
        return f"-H.I.P: {self.hora_inicio_prevista} -H.I: {self.numero} -H.F: {self.hora_inicio} "




        
        
