# Generated by Django 4.2.6 on 2023-10-21 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_alter_asesor_curriculum'),
        ('proyecto_trabajo_final', '0002_movimientos_observacion_alter_movimientos_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectofinal',
            name='asesor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectos_asesor', to='persona.asesor'),
        ),
        migrations.AlterField(
            model_name='proyectofinal',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]