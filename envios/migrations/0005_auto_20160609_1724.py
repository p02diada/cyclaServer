# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0004_auto_20160609_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='telefonoRemitente',
            field=models.CharField(max_length=15),
        ),
    ]
