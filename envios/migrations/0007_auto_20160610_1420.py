# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0006_auto_20160609_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='datosAdicionalesDireccionReceptor',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='datosAdicionalesDireccionRemitente',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='descripcion',
            field=models.TextField(default='', max_length=140),
        ),
    ]
