from django.contrib import admin

# Register your models here.

from .models import Semestre, Formulario, Periodo, Cuenta, Movimiento, Integrante

@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    list_display = ('id', 'año', 'nombre')
    search_fields = ('año', 'nombre')
    list_filter = ('año', 'nombre')

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'trimestre', 'estado')
    search_fields = ('year', 'trimestre')
    list_filter = ('year', 'trimestre', 'estado')
    
admin.site.register(Formulario)

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'tipo')
    search_fields = ('codigo', 'nombre', 'tipo')
    list_filter = ('tipo',)

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    # mostrar los campos id, user, periodo del formulario, cuenta, tipo, descripción
    list_display = ('id', 'user', 'get_formulario_periodo', 'cuenta', 'tipo', 'monto', 'descripcion')
    search_fields = ('user', 'cuenta', 'formulario', 'tipo')
    list_filter = ('tipo',)

    def get_formulario_periodo(self, obj):
        return obj.formulario.periodo
    
    get_formulario_periodo.short_description = 'Periodo'  # Sets column name in admin panel

admin.site.register(Integrante)