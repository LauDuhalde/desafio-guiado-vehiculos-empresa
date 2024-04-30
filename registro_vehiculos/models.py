from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    year = models.IntegerField(null=False)
    activo = models.BooleanField(default=False)

class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    #related_name permite que en Vehiculo se llame a Chofer con el nombre 'chofer'
    vehiculo = models.OneToOneField(Vehiculo,related_name='chofer',blank=True,null=True,on_delete=models.PROTECT)
    # on_delete=models.PROTECT
    # Este argumento especifica que si se intenta eliminar un objeto relacionado 
    # (el objeto al que apunta el ForeignKey o OneToOneField), 
    # Django lanzará una excepción ProtectedError en lugar de eliminar el objeto relacionado.
    
class RegistroContabilidad(models.Model):
    fecha_compra = models.DateField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    vehiculo = models.OneToOneField(Vehiculo, related_name='contabilidad', null=False, blank=False, on_delete=models.PROTECT)
    
