# Generated by Django 4.1.2 on 2022-11-18 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_recorrido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio_prevista', models.DateTimeField(blank=True, null=True)),
                ('hora_inicio', models.DateTimeField(blank=True, null=True)),
                ('hora_fin', models.DateTimeField(blank=True, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('bus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='administracion.bus')),
                ('chofer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='administracion.chofer')),
                ('recorrido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='administracion.recorrido')),
            ],
        ),
    ]
