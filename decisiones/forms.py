from django import forms
from .models import Formulario, Periodo, User, Grupo

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'
        ##widgets = {
        ##    'grupo': forms.Select(attrs={'class': 'form-control'} ),
        ##}
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FormularioForm, self).__init__(*args, **kwargs)
        # seleccionar grupo del usuario actual
        self.fields['grupo'].queryset = Grupo.objects.filter(user=self.user)
        # Filtrar periodos activos
        self.fields['periodo'].queryset = Periodo.objects.filter(estado=True) 
        # Añadir clases a los campos
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            field.widget.attrs.update({'value': '0'})
            field.widget.attrs.update({'min': '0'})

        
