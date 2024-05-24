from django.contrib import admin

# Register your models here.

from .models import Grupo, Formulario

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


admin.site.register(Formulario)