from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Formulario, Grupo
from .forms import FormularioForm

# Create your views here.

def home(request):
    cant_grupos = Grupo.objects.count()
    grupos = Grupo.objects.all()
    return render(request, 'decisiones/home.html', {'cant_grupos':cant_grupos, 'grupos': grupos})


class FormularioNew(CreateView):
    model = Formulario
    template_name = 'decisiones/formulario_form.html'
    form_class = FormularioForm
    success_url = reverse_lazy('home')