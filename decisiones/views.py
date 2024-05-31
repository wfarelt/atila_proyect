from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Formulario, Movimiento, Cuenta
from .forms import FormularioForm

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
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        # COMPRA DE MATERIA PRIMA
        movimiento(self, form, '105', 'DEBE', form.instance.calcular_VIMP(), 'Compra de materia prima')
        movimiento(self, form, '103', 'DEBE', form.instance.calcular_CF(), 'Compra de materia prima')
        movimiento(self, form, '101', 'HABER', form.instance.calcular_CYB(), 'Compra de materia prima')
        # PRODUCCION DE 120
        movimiento(self, form, '104', 'DEBE', form.instance.calcular_VIPT(), 'Producción de 120')
        movimiento(self, form, '105', 'HABER', form.instance.calcular_VIMP2(), 'Producción de 120')
        # PAGO DE PLANILLA DE MANO DE OBRA ESPECIALIZADA
        movimiento(self, form, '403', 'DEBE', form.instance.calcular_CV(), 'Pago de planilla de mano de obra especializada')
        movimiento(self, form, '502', 'DEBE', form.instance.calcular_APL(), 'Pago de planilla de mano de obra especializada')
        messages.success(self.request, 'El registro se ha guardado con éxito.')
        return response

# MOVIMIENTOS
def movimiento(self, form, codigo, tipo, monto, descripcion):
    m = Movimiento.objects.create(
        user=self.request.user,
        cuenta= Cuenta.objects.get(codigo=codigo),
        formulario=form.instance,
        tipo=tipo,
        monto = monto,
        descripcion = descripcion
        )
    m.save()
    return 

# BALANCE GENERAL
def balance_general(request):
    mis_movimientos = Movimiento.objects.filter(user=request.user)
    # ACTIVO
    c1 = total_cuenta(mis_movimientos, '101')
    c2 = total_cuenta(mis_movimientos, '102')
    c3 = total_cuenta(mis_movimientos, '103')
    c4 = total_cuenta(mis_movimientos, '104')
    c5 = total_cuenta(mis_movimientos, '105')
    c6 = total_cuenta(mis_movimientos, '106')
    c7 = total_cuenta(mis_movimientos, '107')
    c8 = total_cuenta(mis_movimientos, '108')
    c9 = total_cuenta(mis_movimientos, '109')
    c10 = total_cuenta(mis_movimientos, '110')
    c11 = total_cuenta(mis_movimientos, '111')
    c12 = total_cuenta(mis_movimientos, '112')
    c13 = total_cuenta(mis_movimientos, '113')
    c14 = total_cuenta(mis_movimientos, '114')
    # PASIVO
    c201 = total_cuenta(mis_movimientos, '201')
    c202 = total_cuenta(mis_movimientos, '202')
    c203 = total_cuenta(mis_movimientos, '203')
    c204 = total_cuenta(mis_movimientos, '204')
    c205 = total_cuenta(mis_movimientos, '205')
    c206 = total_cuenta(mis_movimientos, '206')
    c207 = total_cuenta(mis_movimientos, '207')
    c208 = total_cuenta(mis_movimientos, '208')
    #PATRIMONIO
    c301 = total_cuenta(mis_movimientos, '301')
    c302 = total_cuenta(mis_movimientos, '302')
    c303 = total_cuenta(mis_movimientos, '303')
    # INGRESOS
    c401 = total_cuenta(mis_movimientos, '401')
    c402 = total_cuenta(mis_movimientos, '402')
    c403 = total_cuenta(mis_movimientos, '403')
    c404 = total_cuenta(mis_movimientos, '404')
    # EGRESOS
    c501 = total_cuenta(mis_movimientos, '501')
    c502 = total_cuenta(mis_movimientos, '502')
    c503 = total_cuenta(mis_movimientos, '503')
    c504 = total_cuenta(mis_movimientos, '504')
    c505 = total_cuenta(mis_movimientos, '505')
    c506 = total_cuenta(mis_movimientos, '506')

    context = {
        # ACTIVO
        'c1': c1,
        'c2': c2,
        'c3': c3,
        'c4': c4,
        'c5': c5,
        'c6': c6,
        'c7': c7,
        'c8': c8,
        'c9': c9,
        'c10': c10,
        'c11': c11,
        'c12': c12,
        'c13': c13,
        'c14': c14,
        # PASIVO
        'c201': c201,
        'c202': c202,
        'c203': c203,
        'c204': c204,
        'c205': c205,
        'c206': c206,
        'c207': c207,
        'c208': c208,
        # PATRIMONIO
        'c301': c301,
        'c302': c302,
        'c303': c303,
        # INGRESOS
        'c401': c401,
        'c402': c402,
        'c403': c403,
        'c404': c404,
        # EGRESOS
        'c501': c501,
        'c502': c502,
        'c503': c503,
        'c504': c504,
        'c505': c505,
        'c506': c506,
    }    
    return render(request, 'decisiones/balance_general.html', context)

# Calcular suma de los movimientos de una cuenta
def total_cuenta(movimientos, codigo_cuenta):
    t = 0
    for m in movimientos:
        if m.cuenta.codigo == codigo_cuenta:
            if m.tipo == 'DEBE':
                t -= m.monto
            else:
                t += m.monto
    return t