# Generated by Django 4.0.3 on 2022-05-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0003_rename_categoriaservicio_id_detallecategoria_categoriaservicio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecategoria',
            name='nombre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]