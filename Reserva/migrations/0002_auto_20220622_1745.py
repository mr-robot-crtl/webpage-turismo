# Generated by Django 3.1.7 on 2022-06-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='num_n',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
