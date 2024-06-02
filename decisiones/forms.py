from django import forms
from .models import Formulario, Periodo, Integrante

# FORMULARIO FORM
class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar periodos activos
        self.fields['periodo'].queryset = Periodo.objects.filter(estado=True)
        # Agregar clases de bootstrap
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            # Agregar valor por defecto a los campos numericos
            if 'P' in field:
                self.fields[field].widget.attrs.update({'value': 0})
            # Agregar placeholder a los campos numericos
            if 'P' in field:
                self.fields[field].widget.attrs.update({'placeholder': 'Ingrese un valor'})
             
# INTEGRANTES FORM
class IntegranteForm(forms.ModelForm):
    class Meta:
        model = Integrante
        exclude = ['user']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agregar clases de bootstrap
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})




        
    