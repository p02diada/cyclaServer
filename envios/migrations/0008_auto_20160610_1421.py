# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0007_auto_20160610_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='descripcion',
            field=models.TextField(max_length=140),
        ),
    ]
