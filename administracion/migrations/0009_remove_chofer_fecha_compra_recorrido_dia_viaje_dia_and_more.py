# Generated by Django 4.1.2 on 2022-11-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0008_viaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chofer',
            name='fecha_compra',
        ),
        migrations.AddField(
            model_name='recorrido',
            name='dia',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='viaje',
            name='dia',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='duracion_aprox',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='frecuencia',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='hora_finalizacion',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recorrido',
            name='hora_inicio',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='hora_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='hora_inicio',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='hora_inicio_prevista',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
