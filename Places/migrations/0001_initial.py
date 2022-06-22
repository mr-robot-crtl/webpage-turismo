# Generated by Django 3.1.7 on 2022-06-21 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('cat_lug_image', models.ImageField(blank=True, null=True, upload_to='cat_lug_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('lugar_image', models.ImageField(blank=True, null=True, upload_to='lugar_image/')),
                ('descriptions', models.CharField(max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Places.category_place')),
            ],
        ),
    ]