
# Generated by Django 4.2.6 on 2023-11-01 15:35

# Generated by Django 4.2.6 on 2023-11-01 12:11


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_trabajo_final', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientos',
            name='tipoMovimiento',
            field=models.CharField(blank=True, choices=[('presentacion ptf', 'Presentación PTF'), ('pase a la cstf', 'Pase a la CSTF'), ('dictamen de la cstf sobre el formato del ptf', 'Dictamen de la CSTF sobre el formato del PTF'), ('pase al te', 'Pase al TE'), ('dictamen tribunal evaluador sobre evaluación ptf', 'Dictamen tribunal evaluador sobre evaluación PTF'), ('presentación borrador informe final', 'Presentación borrador Informe final'), ('dictamen tribunal evaluador sobre borrador', 'dictamen tribunal evaluador sobre borrador')], max_length=50, null=True),
        ),
    ]
