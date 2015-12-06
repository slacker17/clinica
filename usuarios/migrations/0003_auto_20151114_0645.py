# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20151114_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='enfermedad',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='paciente',
            name='mejorias',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='paciente',
            name='tratamiento',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
