from django.db import models


# Create your models here.

class Bus(models.Model):
    patente = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    numero_unidad = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    fecha_compra = models.DateField(blank=True, null=True)  # Field name made lowercase.
    estado = models.BooleanField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BUS'
        
        
class Chofer(models.Model):
    legajo = models.CharField(max_length=50, blank=True, null=True)
    fecha_compra = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    nombre= models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHOFER'



class Atractivo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    calificacion = models.FloatField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATRACTIVO'
        
        
        
class Parada(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    foto = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    atractivos = models.ManyToManyField(Atractivo)
    class Meta:
        managed = False
        db_table = 'PARADA'
        
        

class DetalleCadaParada(models.Model):
    numero_orden = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    conexion = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    parada = models.ForeignKey(Parada, models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETALLE_CADA_PARADA'



class Recorrido(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    hora_inicio = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    hora_finalizacion = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    duracion_aprox = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    frecuencia = models.PositiveIntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    lista_detalle_parada = models.ForeignKey(DetalleCadaParada, models.DO_NOTHING,blank=True, null=True)  # Field name made lowercase.
   
    class Meta:
        managed = False
        db_table = 'RECORRIDO'
        


class Viaje(models.Model):
    hora_inicio_prevista = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    hora_inicio = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    hora_fin = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    numero = models.IntegerField(blank=True, null=True)
    bus = models.ForeignKey(Bus, models.DO_NOTHING, blank=True, null=True)
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING, blank=True, null=True)
    recorrido = models.ForeignKey(Recorrido, models.DO_NOTHING,     blank=True, null=True)
    
    
    class Meta:
        managed = False
        db_table = 'VIAJE'
    

