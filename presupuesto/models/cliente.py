from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre



