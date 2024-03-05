from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno
from .formulario import AlumnoForm  # Asegúrate de haber creado AlumnoForm en forms.py

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
