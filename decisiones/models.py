from django.db import models

# Create your models here.

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Formulario(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
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
    P17 = models.IntegerField(verbose_name='Cantidad P17')
    P18 = models.IntegerField(verbose_name='Cantidad P18')
    P19 = models.DecimalField(verbose_name='Bolivianos P19', max_digits=10, decimal_places=2)
    P22 = models.DecimalField(verbose_name='Bolivianos P22', max_digits=10, decimal_places=2)
    P23 = models.DecimalField(verbose_name='Bolivianos P23', max_digits=10, decimal_places=2)
    P24 = models.IntegerField(verbose_name='Cantidad P24')
    P25 = models.IntegerField(verbose_name='Cantidad P25')
    P26 = models.IntegerField(verbose_name='Cantidad P26')
    P27 = models.IntegerField(verbose_name='Cantidad P27')
    P28 = models.IntegerField(verbose_name='Cantidad P28')
    P29 = models.DecimalField(verbose_name='Bolivianos P29', max_digits=10, decimal_places=2)
    P30 = models.IntegerField(verbose_name='Cantidad P30')
    P31 = models.IntegerField(verbose_name='Cantidad P31')
    P33 = models.DecimalField(verbose_name='Bolivianos P33', max_digits=10, decimal_places=2)
    P34 = models.IntegerField(verbose_name='Años P34')
    P35 = models.DecimalField(verbose_name='% P35', max_digits=5, decimal_places=2)
    P36 = models.DecimalField(verbose_name='Bolivianos P36', max_digits=10, decimal_places=2)
    P37 = models.IntegerField(verbose_name='Años P37')
    P38 = models.DecimalField(verbose_name='% P38', max_digits=5, decimal_places=2)
    P40 = models.CharField(verbose_name='Unidad P40', max_length=100)
    P41 = models.DecimalField(verbose_name='Bolivianos P41', max_digits=10, decimal_places=2)
    P42 = models.DecimalField(verbose_name='Bolivianos P42', max_digits=10, decimal_places=2)
    P43 = models.CharField(verbose_name='Unidades P43', max_length=100)
    P45 = models.CharField(verbose_name='Unidades P45', max_length=100)

    def __str__(self):
        return f'Formulario #{self.id}'
    
    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"
