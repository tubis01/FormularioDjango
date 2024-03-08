from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    
    fechaNacimiento = forms.DateField(input_formats=['%d-%m-%Y'])
    class Meta:
        model = Alumno
        fields = ['carnet', 'nombres', 'apellidos', 'correoElectronico', 'fechaNacimiento']


