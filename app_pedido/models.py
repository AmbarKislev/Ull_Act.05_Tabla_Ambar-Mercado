from django.db import models

# Create your models here.
class Pedido(models.Model):
    pedido =  models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

#es para la administracion servidor admin
def __str__(self):
    return f"{self.pedido} {self.fecha}"