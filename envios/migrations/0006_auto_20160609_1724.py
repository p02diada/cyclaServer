# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0005_auto_20160609_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='direccionReceptor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='direccionRemitente',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='nombreReceptor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='nombreRemitente',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='telefonoReceptor',
            field=models.CharField(max_length=15),
        ),
    ]
