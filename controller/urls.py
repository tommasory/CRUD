from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.inicio, name='index'),
    path('crear/', views.crearPersona, name='crear'),
]
