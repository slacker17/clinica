# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido_paterno', models.CharField(max_length=25)),
                ('apellido_materno', models.CharField(max_length=25)),
                ('curp', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_ingreso', models.DateField()),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=40)),
                ('peso', models.FloatField()),
                ('estatura', models.FloatField()),
                ('diagnostico', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
