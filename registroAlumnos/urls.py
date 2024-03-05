# registroAlumnos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crearAlumno/', views.crearAlumno, name='crearAlumno'),
    path('eliminarAlumno/<int:pk>/', views.eliminarAlumno, name='eliminarAlumno'),
    path('listarAlumno/', views.listarAlumno, name='listarAlumno'),
    path('modificarAlumno/<int:pk>/', views.modificarAlumno, name='modificarAlumno'),
]
