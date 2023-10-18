# Generated by Django 4.2.6 on 2023-10-18 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_alter_asesor_curriculum'),
        ('comisiones', '0003_integrantescomision'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntegrantesTribunal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('presidente', 'Presidente'), ('vocal_titular', 'Vocal Titular'), ('vocal_secundario', 'Vocal Secundario')], max_length=16)),
                ('fecha_alta_te', models.DateField()),
                ('fecha_baja_te', models.DateField()),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.docente')),
                ('tribunal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comisiones.tribunalevaluador')),
            ],
            options={
                'ordering': ['fecha_alta_te'],
            },
        ),
    ]
