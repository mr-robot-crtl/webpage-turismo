# Generated by Django 4.0.3 on 2022-05-19 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0002_detallecategoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallecategoria',
            old_name='categoriaservicio_id',
            new_name='categoriaservicio',
        ),
        migrations.RenameField(
            model_name='detallecategoria',
            old_name='planservicio_id',
            new_name='planservicio',
        ),
    ]