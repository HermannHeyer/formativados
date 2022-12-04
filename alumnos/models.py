from django.db import models


# Create your models here.

class Alumnos(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    apellido = models.CharField(max_length=255,verbose_name='Apellido')
    rut = models.CharField(max_length=12, unique=True, verbose_name='R.U.T')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualización')
