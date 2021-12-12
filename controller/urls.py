from django.urls import path, include
from .views import *

urlpatterns = [
    path('',inicio, name='index'),
    path('crear/', crearPersona, name='crear'),
    path('editar_persona/<int:id>/', editarPersona, name='editar_persona'),
    path('eliminar_persona/<int:id>/', eliminarPersona, name='eliminar_persona'),
]
