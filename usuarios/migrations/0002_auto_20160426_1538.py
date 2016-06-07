# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciclista',
            name='latitudUltimoPunto',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ciclista',
            name='longitudUltimoPunto',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
