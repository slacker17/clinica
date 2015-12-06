# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estatura',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_ingreso',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='peso',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
