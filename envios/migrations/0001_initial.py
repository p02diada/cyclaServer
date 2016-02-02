# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('latitudPuntoInicial', models.CharField(max_length=50)),
                ('longitudPuntoInicial', models.CharField(max_length=50)),
                ('latitudPuntoFinal', models.CharField(max_length=50)),
                ('longitudPuntoFinal', models.CharField(max_length=50)),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Remitente')),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='envios.Anuncio')),
                ('ciclista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Ciclista')),
            ],
        ),
    ]