# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0002_anuncio_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='estado',
            field=models.CharField(default='esperando', max_length=50, choices=[('esperando', 'esperando'), ('enviando', 'enviando'), ('entregado', 'entregado')]),
        ),
    ]
