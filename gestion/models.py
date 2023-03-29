from django.db import models

class Productos(models.Model):
    producto = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=30)
    precio= models.IntegerField

class Categorias(models.Model):
    nombre = models.TextField(max_length=20)
    descripcion = models.TextField(max_length=30)
# Create your models here.
