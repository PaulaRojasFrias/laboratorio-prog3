# Generated by Django 4.2.6 on 2023-10-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('matricula', models.CharField(max_length=5, unique=True)),
                ('correo', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ('apellido', 'nombre'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
                ('curriculum', models.FileField(upload_to='archivosCurriculums')),
            ],
            options={
                'ordering': ('apellido', 'nombre'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
                ('cuil', models.CharField(max_length=11, unique=True)),
            ],
            options={
                'ordering': ('apellido', 'nombre'),
                'abstract': False,
            },
        ),
    ]