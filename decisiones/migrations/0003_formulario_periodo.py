# Generated by Django 5.0.4 on 2024-05-29 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decisiones', '0002_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='periodo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formularios', to='decisiones.periodo'),
        ),
    ]