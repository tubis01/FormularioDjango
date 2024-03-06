from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno
from .formulario import AlumnoForm  # Asegúrate de haber creado AlumnoForm en forms.py
from collections import Counter #para contar los alumnos que hay de cada edad
from datetime import date

# Vista para listar alumnos
def listarAlumno(request):
    alumnos = Alumno.objects.all()
    return render(request, 'registroAlumnos/listarAlumno.html', {'alumnos': alumnos})

# Vista para crear alumno
def crearAlumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarAlumno')
    else:
        form = AlumnoForm()
    return render(request, 'registroAlumnos/crearAlumno.html', {'form': form})

# Vista para modificar alumno
def modificarAlumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('listarAlumno')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'registroAlumnos/modificarAlumno.html', {'form': form})

# Vista para eliminar alumno
def eliminarAlumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('listarAlumno')
    return render(request, 'registroAlumnos/eliminarAlumno.html', {'alumno': alumno})

# vista para estadisticas de alumnos por edad
def estadisticas_edad(request):
    alumnos = Alumno.objects.all()
    edades = [calcular_edad(alumno.fechaNacimiento) for alumno in alumnos]
    conteo_edades = Counter(edades)
    estadisticas = sorted(conteo_edades.items())
    return render(request, 'registroAlumnos/estadisticasEdad.html', {'estadisticas': estadisticas})



def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad
