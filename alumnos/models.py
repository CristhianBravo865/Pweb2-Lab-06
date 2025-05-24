from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre