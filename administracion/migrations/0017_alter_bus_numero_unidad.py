# Generated by Django 4.1.2 on 2022-12-01 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0016_alter_bus_fecha_compra_alter_bus_numero_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='numero_unidad',
            field=models.IntegerField(),
        ),
    ]
