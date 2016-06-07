# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='estado',
            field=models.CharField(default='activo', max_length=50, choices=[('caducado', 'caducado'), ('activo', 'activo')]),
        ),
    ]
