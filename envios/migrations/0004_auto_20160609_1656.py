# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0003_auto_20160425_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='direccionReceptor',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='direccionRemitente',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='nombreReceptor',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='nombreRemitente',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='telefonoReceptor',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='telefonoRemitente',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='envio',
            name='estado',
            field=models.CharField(default='esperando', max_length=50, choices=[('esperando', 'esperando'), ('enviando', 'enviando'), ('entregado', 'entregado'), ('confirmado', 'confirmado')]),
        ),
    ]
