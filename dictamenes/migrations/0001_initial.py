# Generated by Django 4.2.6 on 2023-10-31 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comisiones', '0001_initial'),
        ('proyecto_trabajo_final', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefensaOral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDefensa', models.DateField()),
                ('notaObtenida', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionPTF_TE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultadoTE', models.CharField(choices=[('aprobado', 'Aprobado'), ('observado', 'Observado'), ('rechazado', 'Rechazado')], max_length=256)),
                ('observaciones', models.CharField(blank=True, max_length=256, null=True)),
                ('informeEvaluacionTE', models.FileField(blank=True, null=True, upload_to='archivosDictamenes/')),
                ('fechaEvaluacionTE', models.DateField()),
                ('evaluadorTE', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='comisiones.tribunalevaluador')),
                ('ptf_evaluadoTE', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proyecto_trabajo_final.proyectofinal')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionPTF_CSTF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultadoCSTF', models.CharField(choices=[('aprobado', 'Aprobado'), ('observado', 'Observado'), ('rechazado', 'Rechazado')], max_length=256)),
                ('observaciones', models.CharField(blank=True, max_length=256, null=True)),
                ('informeEvaluacionCSTF', models.FileField(blank=True, null=True, upload_to='archivosDictamenes/')),
                ('fechaEvaluacionCSTF', models.DateField()),
                ('evaluadorCSTF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comisiones.comision')),
                ('ptf_evaluadoCSTF', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proyecto_trabajo_final.proyectofinal')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionITF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultadoITF', models.CharField(choices=[('aprobado', 'Aprobado'), ('observado', 'Observado'), ('rechazado', 'Rechazado')], max_length=256)),
                ('observaciones', models.CharField(max_length=256)),
                ('informeEvaluacionITF', models.FileField(blank=True, null=True, upload_to='archivosDictamenes/')),
                ('fechaEvaluacionITF', models.DateField()),
                ('evaluadorTE_ITF', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='comisiones.tribunalevaluador')),
                ('itf_evaluadoTE', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proyecto_trabajo_final.informetf')),
            ],
        ),
    ]
