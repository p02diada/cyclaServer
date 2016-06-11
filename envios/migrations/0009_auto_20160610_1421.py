# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0008_auto_20160610_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='datosAdicionalesDireccionReceptor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='datosAdicionalesDireccionRemitente',
            field=models.CharField(max_length=50),
        ),
    ]
