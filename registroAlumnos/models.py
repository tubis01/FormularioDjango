from django.db import models

# Create your models here.

from django.db import models

class Alumno(models.Model):
    carnet = models.CharField(max_length=15, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correoElectronico = models.EmailField()
    fechaNacimiento = models.DateField()

    def __str__(self):
        return self.nombres + ' ' + self.apellidos
