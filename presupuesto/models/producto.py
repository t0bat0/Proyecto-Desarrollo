from django.db import models


class Accesorio(models.Model):
    nombre = models.CharField(max_length=500, null=True)
    descripcion = models.TextField(max_length=1000)
    precio_accesorio = models.IntegerField(blank=True, null=True)
    proveedor = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre

   

class Producto(models.Model):
    nombre = models.CharField(max_length=500, null=True)
    descripcion = models.TextField(max_length=1000)
    profundidad = models.FloatField(default=70, blank=True, null=True)
    alto = models.FloatField(blank=True, null=True)
    ancho = models.FloatField(blank=True, null=True)
    tipo_de_terminacion=models.CharField(max_length=500,blank=True, null=True)  
    precio_producto = models.IntegerField(blank=True, null=True)
    proveedor = models.CharField(max_length=100,blank=True, null=True)
    accesorios = models.ManyToManyField(Accesorio,blank=True, null=True)
    def __str__(self):
        return self.nombre