from django.db import models

# Create your models here.
class Usuarios(models.Model):
    usuario = models.CharField(max_length=100)
    fecha_ingreso = models.CharField(max_length=20)    
    hora_ingreso = models.CharField(max_length=10)
    pais = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    tiempo = models.CharField(max_length=20)
    ruta = models.CharField(max_length=200)
    dispositivo = models.CharField(max_length=20)