# Generated by Django 4.2.6 on 2023-10-21 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_alter_asesor_curriculum'),
        ('proyecto_trabajo_final', '0003_alter_proyectofinal_asesor_alter_proyectofinal_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ptf_integrantes',
            name='alumnos',
        ),
        migrations.AddField(
            model_name='ptf_integrantes',
            name='alumnos',
            field=models.ManyToManyField(related_name='proyectos', to='persona.alumno'),
        ),
    ]
