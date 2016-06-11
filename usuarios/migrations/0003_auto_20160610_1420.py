# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20160426_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciclista',
            name='cantidadValoraciones',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ciclista',
            name='valoracionMedia',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
