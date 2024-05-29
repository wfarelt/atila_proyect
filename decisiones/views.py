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
    return render(request, 'decisiones/home.html')


#FORMULARIOS

class FormularioListView(ListView):
    model = Formulario
    template_name = 'decisiones/formulario_list.html'
    context_object_name = 'formularios'

class FormularioCreateView(CreateView):
    model = Formulario
    template_name = 'decisiones/formulario_form.html'
    form_class = FormularioForm
    success_url = reverse_lazy('formulario_new')

    def get_form_kwargs(self):
        kwargs = super(FormularioCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El registro se ha guardado con éxito.')
        return response
    
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
    
# GRUPOS

class GrupoListView(ListView):
    model = Grupo
    template_name = 'decisiones/grupo_list.html'
    context_object_name = 'grupos'

class GrupoCreateView(CreateView):
    model = Grupo
    template_name = 'decisiones/grupo_form.html'
    fields = '__all__'
    success_url = reverse_lazy('grupo_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El registro se ha guardado con éxito.')
        return response

class GrupoUpdateView(UpdateView):
    model = Grupo
    template_name = 'decisiones/grupo_form.html'
    fields = '__all__'
    context_object_name = 'obj'
    success_url = reverse_lazy('grupo_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'El registro se ha actualizado con éxito.')
        return response