# Generated by Django 4.1.2 on 2022-12-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0020_alter_bus_estado_alter_bus_numero_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='fecha_compra',
            field=models.DateField(),
        ),
    ]