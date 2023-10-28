# Generated by Django 4.2.6 on 2023-10-28 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto_trabajo_final', '0001_initial'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDeCreacionComision', models.DateField()),
                ('nroResolucionComision', models.CharField(max_length=30, unique=True)),
                ('archivoResolucion', models.FileField(upload_to='archivosComisiones/')),
            ],
            options={
                'ordering': ['fechaDeCreacionComision'],
            },
        ),
        migrations.CreateModel(
            name='TribunalEvaluador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroDisposicionTribunal', models.CharField(max_length=50, unique=True)),
                ('fechaCreacionTribunal', models.DateField()),
                ('archivoDisposicion', models.FileField(upload_to='archivosComisiones/')),
                ('proyectoTE', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proyecto_trabajo_final.proyectofinal')),
            ],
            options={
                'ordering': ['fechaCreacionTribunal'],
            },
        ),
        migrations.CreateModel(
            name='IntegrantesTribunal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('presidente', 'Presidente'), ('vocal_titular', 'Vocal Titular'), ('vocal_secundario', 'Vocal Secundario')], max_length=16)),
                ('fecha_alta_te', models.DateField()),
                ('fecha_baja_te', models.DateField(blank=True, null=True)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.docente')),
                ('tribunal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comisiones.tribunalevaluador')),
            ],
            options={
                'ordering': ['fecha_alta_te'],
            },
        ),
        migrations.CreateModel(
            name='IntegrantesComision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_alta_cs', models.DateField()),
                ('fecha_baja_cs', models.DateField(blank=True, null=True)),
                ('comision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comisiones.comision')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.docente')),
            ],
            options={
                'ordering': ['fecha_alta_cs'],
            },
        ),
    ]
