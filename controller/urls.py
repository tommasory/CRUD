from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PersonaList.as_view(), name='index'),
    path('crear_persona/', PersonaCreate.as_view(), name='crear_persona'),
    path('editar_persona/<int:pk>/', PersonaUpdate.as_view(), name='editar_persona'),
    path('eliminar_persona/<int:pk>/', PersonaDelete.as_view(),name='eliminar_persona'),
]
