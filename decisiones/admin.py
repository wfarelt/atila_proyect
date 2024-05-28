from django.contrib import admin

# Register your models here.

from .models import Semestre, Grupo, Formulario

@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    list_display = ('id', 'año', 'nombre')
    search_fields = ('año', 'nombre')
    list_filter = ('año', 'nombre')

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


admin.site.register(Formulario)