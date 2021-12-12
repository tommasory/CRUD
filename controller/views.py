from django.shortcuts import render
from . import models

# Create your views here.
def inicio(request):
    personas = models.Persona.objects.all()
    contexto = {'personas':personas}
    return render (request, 'index.html',contexto)