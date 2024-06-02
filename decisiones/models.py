from django.db import models

# Create your models here.

# SEMESTRES
class Semestre(models.Model):
    año = models.IntegerField()
    nombre = models.CharField(max_length=10)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"
        ordering = ['año', 'nombre']

    #mostrar año y nombre
    def __str__(self):
        return f'{self.año} - {self.nombre}'

# PERIODOS
class Periodo(models.Model):
    year = models.IntegerField()
    trimestre = models.IntegerField()
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"
        ordering = ['year', 'trimestre']
    
    def __str__(self):
        return f'{self.year} - Trimestre {self.trimestre}'
    
#FORMULARIOS
class Formulario(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='formularios', null=True, blank=True)
    periodo = models.ForeignKey('Periodo', on_delete=models.CASCADE, related_name='formularios', null=True, blank=True)
    P4 = models.IntegerField(verbose_name='Indique la cantidad total de personal especializado de mano de obra de producción en un trimestre (en cantidad)')
    P5 = models.IntegerField(verbose_name='El total de personal especializado como máximo puede producir un total de unidades de productos terminados en trimestre de: (en cantidad)')
    P6 = models.DecimalField(verbose_name='Solo un personal especializado de mano de obra de producción en promedio tiene un costo trimestral de bolivianos. (Una sola persona)', max_digits=10, decimal_places=2)
    P8 = models.DecimalField(verbose_name='¿Cuál es el precio de Materia Prima incluye: materia prima e insumos de fabricación?  (Bs. por unidad)', max_digits=10, decimal_places=2)
    P9 = models.IntegerField(verbose_name='¿Cuántas unidades comprará de Materia Prima (materia prima e insumos)  para este trimestre (en cantidad)')
    P10 = models.IntegerField(verbose_name='¿Cuál es su capacidad máxima de producción unidades en un trimestre?  (en cantidad)')
    P11 = models.DecimalField(verbose_name='Precio de cada máquina', max_digits=10, decimal_places=2)
    P12 = models.IntegerField(verbose_name='¿Cuál es el número de máquinas que comprará para este trimestre?')
    P13 = models.IntegerField(verbose_name='Cada máquina comprada ¿Cuántas unidades produce en promedio?')
    P15 = models.IntegerField(verbose_name='¿Qué cantidad de personal especializado contratará para este trimestre (en cantidad)')
    P16 = models.IntegerField(verbose_name='¿Qué cantidad de personal especializado despedirá para este trimestre (en cantidad)')
    P17 = models.IntegerField(verbose_name='¿Qué cantidad de Personal administrativo contratará para este trimestre?  (en cantidad)')
    P18 = models.IntegerField(verbose_name='¿Qué cantidad de Personal administrativo despedirá para este trimestre? (en cantidad)')
    P19 = models.DecimalField(verbose_name='Para solo un personal administrativo ¿Cuál es el costo en promedio por trimestre en bolivianos?. (Una sola persona)', max_digits=10, decimal_places=2)
    P22 = models.DecimalField(verbose_name='¿Cuál será su Precio de Venta con factura? (Bs. por unidad)', max_digits=10, decimal_places=2)
    P23 = models.DecimalField(verbose_name='¿Cuál será su Precio de Venta con factura a distribuidores? (Bs. por unidad)', max_digits=10, decimal_places=2)
    P24 = models.IntegerField(verbose_name='¿Qué cantidad de Distribuidores contratará en este trimestre? (en cantidad)')
    P25 = models.IntegerField(verbose_name='¿Qué cantidad de Distribuidores despedirá en este trimestre? (en cantidad)')
    P26 = models.IntegerField(verbose_name='Publicidad Alcance: ¿Cuál es la cantidad de personas que alcanzará para este trimestre con su publicidad?')
    P27 = models.IntegerField(verbose_name='Publicidad frecuencia: ¿Cuál es la cantidad de salidas para este trimestre? (cantidad de veces por trimestre)')
    P28 = models.IntegerField(verbose_name='Indique el tiempo o la cantidad de minutos destinado por cada salida para un trimestre (introducir cuantos minutos son por una salida/trimestre)')
    P29 = models.DecimalField(verbose_name='¿Cuál es el precio en bolivianos por cada minuto de publicidad?', max_digits=10, decimal_places=2)
    P30 = models.IntegerField(verbose_name='Cantidad de unidades a vender de su pronóstico en ventas para este trimestre')
    P31 = models.IntegerField(verbose_name='Cantidad de unidades a vender de su pronóstico en ventas para el próximo trimestre')
    P33 = models.DecimalField(verbose_name='Solicitud de monto de crédito operativo en bolivianos al Banco  (Monto en bolivianos)', max_digits=10, decimal_places=2)
    P34 = models.IntegerField(verbose_name='Tiempo de crédito operativo en bolivianos al Banco  (años)')
    P35 = models.DecimalField(verbose_name='Tasa de crédito operativo en bolivianos al Banco  (años)', max_digits=5, decimal_places=2)
    P36 = models.DecimalField(verbose_name='Solicitud de monto de crédito de inversión en bolivianos al Banco  (Monto en bolivianos)', max_digits=10, decimal_places=2)
    P37 = models.IntegerField(verbose_name='Tiempo de crédito de inversión en bolivianos al Banco  (años)')
    P38 = models.DecimalField(verbose_name='Tasa de crédito de inversión en bolivianos al Banco  (años)', max_digits=5, decimal_places=2)
    P40 = models.CharField(verbose_name='Innovación: Una unidad de materia prima equivale a una unidad de producto terminado para el primer trimestre 1-2024', max_length=100)
    P41 = models.DecimalField(verbose_name='Para ampliar el tamaño de infraestructura actual (su casa propia) que cubra un espacio igual al de su capacidad de producción actual tiene un costo de', max_digits=10, decimal_places=2)
    P42 = models.DecimalField(verbose_name='El alquiler mensual que le cobran sus padres por usar su infraestructura a partir del 2do trimestre 2024 es de ', max_digits=10, decimal_places=2)
    P43 = models.CharField(verbose_name='Cantidad de unidades a producir', max_length=100)
    P45 = models.CharField(verbose_name='Cantidad de unidades a vender en este trimestre', max_length=100)

    def __str__(self):
        return f'Formulario #{self.id} - Grupo: {self.user}'
    
    # mostrar el periodo del formulario
    def get_periodo(self):
        return self.periodo

    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"

    # crear una función que calcule CYB= P8*P9
    def calcular_CYB(self):
        return self.P8 * self.P9
    
    # Valor invetario Materia Prima
    def calcular_VIMP(self):
        return float(self.calcular_CYB()) * 0.87
    
    # Credito Fiscal
    def calcular_CF(self):
        return float(self.calcular_CYB()) * 0.13
    
    # Valor Inventario Productos Terminados
    def calcular_VIPT(self):
        return float(self.P9) * float(self.P8)*0.87*float(self.P40)

    # Valor Inventario Materia Prima
    def calcular_VIMP2(self):
        return float(self.P9) * float(self.P8)*0.87
    
    # (-) Costo de venta: Salarios Mano de obra
    def calcular_CV(self):
        total_ganado = float(self.P6) * float(self.P15)
        aportes_laborares = total_ganado * 0.1271
        return total_ganado - aportes_laborares
    
    # Aporte patronales y laborales
    def calcular_APL(self):
        total_ganado = float(self.P6) * float(self.P15)
        return total_ganado * 0.1671

# CUENTAS
class Cuenta(models.Model):
    TIPO_CUENTA_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('PASIVO', 'Pasivo'),
        ('PATRIMONIO', 'Patrimonio'),
        ('INGRESO', 'Ingreso'),
        ('GASTO', 'Gasto'),
    ]

    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CUENTA_CHOICES)
    
    def __str__(self):
        return f'{self.codigo} - {self.nombre}'
    
    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"

# MOVIMIENTOS
class Movimiento(models.Model):
    TIPO_CUENTA_CHOICES = [
        ('DEBE', 'Debe'),
        ('HABER', 'Haber'),
    ]
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='movimientos')
    cuenta = models.ForeignKey('Cuenta', on_delete=models.CASCADE, related_name='movimientos')
    formulario = models.ForeignKey('Formulario', on_delete=models.CASCADE, related_name='movimientos')
    tipo = models.CharField(max_length=10, choices=TIPO_CUENTA_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.cuenta} - {self.monto}'
    
    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"

# INTEGRANTES
class Integrante(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='integrantes', null=True, blank=True)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    registro = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.apellido_paterno} {self.apellido_materno} {self.nombre}'
    
    class Meta:
        verbose_name = "Integrante"
        verbose_name_plural = "Integrantes"