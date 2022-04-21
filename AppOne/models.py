from django.db import models

# Create your models here.
class Integrantes(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechaDnacimiento = models.CharField(max_length=30)
 
