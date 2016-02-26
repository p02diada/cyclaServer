# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('latitudPuntoInicial', models.CharField(max_length=50)),
                ('longitudPuntoInicial', models.CharField(max_length=50)),
                ('latitudPuntoFinal', models.CharField(max_length=50)),
                ('longitudPuntoFinal', models.CharField(max_length=50)),
                ('remitente', models.ForeignKey(to='usuarios.Remitente')),
            ],
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=50, choices=[('esperando', 'esperando'), ('enviando', 'enviando'), ('entregado', 'entregado')])),
                ('anuncio', models.ForeignKey(to='envios.Anuncio')),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.IntegerField()),
                ('anuncio', models.ForeignKey(to='envios.Anuncio')),
                ('ciclista', models.ForeignKey(to='usuarios.Ciclista')),
            ],
        ),
        migrations.AddField(
            model_name='envio',
            name='oferta',
            field=models.ForeignKey(to='envios.Oferta'),
        ),
    ]
