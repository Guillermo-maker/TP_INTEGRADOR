# Generated by Django 4.1.2 on 2022-11-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atractivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('calificacion', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ATRACTIVO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.IntegerField(blank=True, null=True)),
                ('numero_unidad', models.IntegerField(blank=True, null=True)),
                ('fecha_compra', models.DateField(blank=True, null=True)),
                ('estado', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'BUS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_compra', models.DateTimeField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'CHOFER',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleCadaParada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_orden', models.IntegerField(blank=True, null=True)),
                ('conexion', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'DETALLE_CADA_PARADA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('foto', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'PARADA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recorrido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('hora_inicio', models.DateTimeField(blank=True, null=True)),
                ('hora_finalizacion', models.DateTimeField(blank=True, null=True)),
                ('duracion_aprox', models.IntegerField(blank=True, null=True)),
                ('frecuencia', models.PositiveIntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'RECORRIDO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio_prevista', models.DateTimeField(blank=True, null=True)),
                ('hora_inicio', models.DateTimeField(blank=True, null=True)),
                ('hora_fin', models.DateTimeField(blank=True, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'VIAJE',
                'managed': False,
            },
        ),
    ]
