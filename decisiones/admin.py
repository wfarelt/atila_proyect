from django.contrib import admin

# Register your models here.

from .models import Semestre, Grupo, Formulario, Periodo

@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    list_display = ('id', 'año', 'nombre')
    search_fields = ('año', 'nombre')
    list_filter = ('año', 'nombre')

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'trimestre', 'estado')
    search_fields = ('year', 'trimestre')
    list_filter = ('year', 'trimestre', 'estado')
    
admin.site.register(Formulario)