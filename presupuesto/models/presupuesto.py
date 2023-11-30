from django.db import models
from django.utils.text import slugify
from .cliente import Cliente
from .producto import Producto , Accesorio 


class Presupuesto(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,blank=True)
    id_cliente=models.ForeignKey(Cliente, on_delete= models.CASCADE)
    id_producto = models.ManyToManyField(Producto, through='PresupuestoProducto')

    def save(self,*args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Presupuesto,self).save(*args, **kwargs)
    def __str__(self):
        return self.nombre

class PresupuestoProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,related_name='presupuesto_productos')
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)
    producto_cantidad = models.IntegerField()
    profundidad = models.FloatField( blank=True, null=True)
    #alto = models.FloatField( blank=True, null=True, help_text="Si se deja en blanco se calcula con el alto del producto") es para dar aclaraciones 
    alto = models.FloatField( blank=True, null=True, )
    ancho = models.FloatField(blank=True, null=True)
    tipo_de_terminacion=models.CharField(max_length=500,blank=True, null=True)  
    precio_producto = models.IntegerField(blank=True, null=True)
    id_accesorio = models.ManyToManyField(Accesorio, through='PresupuestoProductoAccesorio',related_name='presupuesto_accesorios', blank=True)
    def subtotal(self):
        subtotal_producto = self.producto_cantidad * (self.precio_producto + self.alto+self.ancho+self.profundidad)
        subtotal_accesorios = sum(accesorio.precio_accesorio for accesorio in self.id_accesorio.all())
        subtotal_accesorios = subtotal_accesorios * self.producto_cantidad
        print(subtotal_accesorios)
        #print(self.id_accesorio)
        return subtotal_producto + subtotal_accesorios

    def save(self,*args, **kwargs):
        if not self.pk:
            if not self.alto:
                self.alto=self.producto.alto
            if not self.ancho:
                self.ancho=self.producto.ancho
            if not self.profundidad:
                self.profundidad=self.producto.profundidad
            if not self.tipo_de_terminacion:
                self.tipo_de_terminacion=self.producto.tipo_de_terminacion

            
                
                
        super(PresupuestoProducto,self).save(*args, **kwargs)
        
            
    
    #todo producto tiene los valores por default y a la hora de crear un presupuesto aparecen drop down de los productos y cuando selecionas un producto aparecen todos los campos por default que luego se pueden modificcar el cual va a modificar el precio dependiendo de distintas variables 
    #productos generales que cambian solo en Presupuesto producto
    #falta calcular el precio con iva
    
    
class PresupuestoProductoAccesorio(models.Model):
    accesorio = models.ForeignKey(Accesorio, on_delete=models.CASCADE)
    presupuesto_producto = models.ForeignKey(PresupuestoProducto, on_delete=models.CASCADE)
    def precio(self):
        print(self.accesorio.precio_accesorio)
        return self.accesorio.precio_accesorio



     

