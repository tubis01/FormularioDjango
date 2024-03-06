from django.db import models

# Create your models here.

from django.db import models
# agragamos la libreria para poder calcular la edad 
from datetime import date

# definimos nuestro model de Alumno 'los campos que contendra'
class Alumno(models.Model):
    carnet = models.CharField(max_length=15, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correoElectronico = models.EmailField()
    fechaNacimiento = models.DateField()

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

# funcion para calcular la edad
def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
