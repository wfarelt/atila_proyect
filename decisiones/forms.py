from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'
        ##widgets = {
        ##    'grupo': forms.Select(attrs={'class': 'form-control'} ),
        ##}
    
    def __init__(self, *args, **kwargs):
        super(FormularioForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            field.widget.attrs.update({'value': '0'})
            field.widget.attrs.update({'min': '0'})
            
