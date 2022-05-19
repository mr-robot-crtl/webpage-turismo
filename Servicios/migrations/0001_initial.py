# Generated by Django 4.0.3 on 2022-05-17 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='movilidad')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'movilidad',
                'verbose_name_plural': 'movilidades',
            },
        ),
        migrations.CreateModel(
            name='PlanServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='plan-servicio')),
                ('descripcion', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'plan',
                'verbose_name_plural': 'planes',
            },
        ),
        migrations.CreateModel(
            name='CategoriaServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='categoria-servicios')),
                ('descripcion', models.CharField(max_length=200)),
                ('costo', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('movilidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicios.movilidad')),
                ('planes', models.ManyToManyField(to='Servicios.planservicio')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
    ]