from .models import *
from .forms import PersonaForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all()[:]

class PersonaCreate (CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaUpdate (UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaDelete (DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')