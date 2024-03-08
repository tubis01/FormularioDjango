from django.db import models
from django.db import models
from datetime import date

class Alumno(models.Model):
    carnet = models.CharField(max_length=15, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correoElectronico = models.EmailField()
    fechaNacimiento = models.DateField()

    def __str__(self):
        return self.nombres + ' ' + self.apellidos


def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
