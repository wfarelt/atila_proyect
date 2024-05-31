from django.core.management.base import BaseCommand
from decisiones.models import Semestre, Periodo, Cuenta

class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        #Semestre.objects.create(año=2024, nombre='I', estado=True)
        #User.objects.create(username='wfarel', password='wf12345*', staff=True, superuser=True)
        #Periodo.objects.create(year=2024, trimestre=1, estado=True)
        #Cuentas [ACTIVOS=[Caja y Bancos, Deudores, Crédito Fiscal, Valor Inventario Productos terminados
        # Valor Inventario Materia Prima, Valor Inmueble, Valor Maquinaria, Muebles y enseres
        # Vehiculos, Herramientas, Equipos de computación, Patente, Inversiones, Depreciaciones]
        Cuenta.objects.create(codigo='101', nombre='Caja y Bancos', tipo='ACTIVO')
        Cuenta.objects.create(codigo='102', nombre='Deudores', tipo='ACTIVO')
        Cuenta.objects.create(codigo='103', nombre='Crédito Fiscal', tipo='ACTIVO')
        Cuenta.objects.create(codigo='104', nombre='Valor Inventario Productos terminados', tipo='ACTIVO')
        Cuenta.objects.create(codigo='105', nombre='Valor Inventario Materia Prima', tipo='ACTIVO')
        Cuenta.objects.create(codigo='106', nombre='Valor Inmueble', tipo='ACTIVO')
        Cuenta.objects.create(codigo='107', nombre='Valor Maquinaria', tipo='ACTIVO')
        Cuenta.objects.create(codigo='108', nombre='Muebles y enseres', tipo='ACTIVO')
        Cuenta.objects.create(codigo='109', nombre='Vehiculos', tipo='ACTIVO')
        Cuenta.objects.create(codigo='110', nombre='Herramientas', tipo='ACTIVO')
        Cuenta.objects.create(codigo='111', nombre='Equipos de computación', tipo='ACTIVO')
        Cuenta.objects.create(codigo='112', nombre='Patente', tipo='ACTIVO')
        Cuenta.objects.create(codigo='113', nombre='Inversiones', tipo='ACTIVO')
        Cuenta.objects.create(codigo='114', nombre='Depreciaciones', tipo='ACTIVO')
        #PASIVOS=[Acreedores, Aportes patronales y laborales x pagar, IVA por pagar, IT por pagar, 
        # IUE por pagar, Beneficios sociales por pagar, Crédito Bancario corto plazo, Crédito Bancario largo plazo]
        Cuenta.objects.create(codigo='201', nombre='Acreedores', tipo='PASIVO')
        Cuenta.objects.create(codigo='202', nombre='Aportes patronales y laborales x pagar', tipo='PASIVO')
        Cuenta.objects.create(codigo='203', nombre='IVA por pagar', tipo='PASIVO')
        Cuenta.objects.create(codigo='204', nombre='IT por pagar', tipo='PASIVO')
        Cuenta.objects.create(codigo='205', nombre='IUE por pagar', tipo='PASIVO')
        Cuenta.objects.create(codigo='206', nombre='Beneficios sociales por pagar', tipo='PASIVO')
        Cuenta.objects.create(codigo='207', nombre='Crédito Bancario corto plazo', tipo='PASIVO')
        Cuenta.objects.create(codigo='208', nombre='Crédito Bancario largo plazo', tipo='PASIVO')
        #PATRIMONIO=[Capital Social, Utilidad de la gestión, Utilidad acumulada]
        Cuenta.objects.create(codigo='301', nombre='Capital Social', tipo='PATRIMONIO')
        Cuenta.objects.create(codigo='302', nombre='Utilidad de la gestión', tipo='PATRIMONIO')
        Cuenta.objects.create(codigo='303', nombre='Utilidad acumulada', tipo='PATRIMONIO')
        #INGRESOS=[Ingresos por Ventas, (-) Costo de venta: Costo de Materia Prima e insumos, (-) Costo de venta: Salarios Mano de obra, Otros ingresos]
        Cuenta.objects.create(codigo='401', nombre='Ingresos por Ventas', tipo='INGRESO')
        Cuenta.objects.create(codigo='402', nombre='(-) Costo de venta: Costo de Materia Prima e insumos', tipo='INGRESO')
        Cuenta.objects.create(codigo='403', nombre='(-) Costo de venta: Salarios Mano de obra', tipo='INGRESO')
        Cuenta.objects.create(codigo='404', nombre='Otros ingresos', tipo='INGRESO')
        #EGRESOS=[Gastos administración, Aporte patronales y laborales, Planilla de Sueldos administrativos, Indemnización y aguinaldo,
        # Gastos de marketing, Impuesto a las transacciones, Depreciación, Amortización inversión diferida, Intereses, Impuestos]
        Cuenta.objects.create(codigo='501', nombre='Gastos administración', tipo='GASTO')
        Cuenta.objects.create(codigo='502', nombre='Aporte patronales y laborales', tipo='GASTO')
        Cuenta.objects.create(codigo='503', nombre='Planilla de Sueldos administrativos', tipo='GASTO')
        Cuenta.objects.create(codigo='504', nombre='Indemnización y aguinaldo', tipo='GASTO')
        Cuenta.objects.create(codigo='505', nombre='Gastos de marketing', tipo='GASTO')
        Cuenta.objects.create(codigo='506', nombre='Impuesto a las transacciones', tipo='GASTO')
        Cuenta.objects.create(codigo='507', nombre='Depreciación', tipo='GASTO')
        Cuenta.objects.create(codigo='508', nombre='Amortización inversión diferida', tipo='GASTO')
        Cuenta.objects.create(codigo='509', nombre='Intereses', tipo='GASTO')
        Cuenta.objects.create(codigo='510', nombre='Impuestos', tipo='GASTO')

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))