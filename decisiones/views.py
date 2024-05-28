from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Formulario, Grupo
from .forms import FormularioForm

# Create your views here.
from django.contrib.auth.admin import User
from django.contrib.auth.views import LoginView, LogoutView

class Login(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

def home(request):
    migrupo = Grupo.get_group(request.user)
    cant_grupos = Grupo.objects.count()
    grupos = Grupo.objects.all()
    return render(request, 'decisiones/home.html', {'cant_grupos':cant_grupos, 'grupos': grupos , 'migrupo': migrupo})

class FormularioNew(CreateView):
    model = Formulario
    template_name = 'decisiones/formulario_form.html'
    form_class = FormularioForm
    success_url = reverse_lazy('formulario_new')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El registro se ha guardado con éxito.')
        return response

# Formulario view
class FormularioList(ListView):
    model = Formulario
    template_name = 'decisiones/formulario_list.html'
    context_object_name = 'formularios'

# Formulario2
class FormularioView(DetailView):
    model = Formulario
    template_name = 'decisiones/formulario2.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["formularios"] = Formulario.objects.all()
        context["titulo"] = "Formulario 3"
        return context