from __future__ import unicode_literals

from django.db import models
from usuarios.models import Ciclista, Remitente
# Create your models here.

class Anuncio(models.Model):
	"""
		Clase que representa un anuncio publicado por un Remitente
	"""
	ESTADOS_ANUNCIO=(
		('caducado', 'caducado'),
		('activo', 'activo'),
		
	)

	remitente= models.ForeignKey(Remitente)
	descripcion=models.TextField(null = True, blank = True)
	latitudPuntoInicial= models.CharField(max_length=50)
	longitudPuntoInicial= models.CharField(max_length=50)
	latitudPuntoFinal= models.CharField(max_length=50)
	longitudPuntoFinal= models.CharField(max_length=50)
	estado=models.CharField(max_length=50, choices=ESTADOS_ANUNCIO, default='activo')


	def __unicode__(self):
		return unicode(self.descripcion)


class Oferta(models.Model):
	"""
		Clase que representa la oferta realizada por un ciclista para un Anuncio
	"""
	anuncio=models.ForeignKey(Anuncio)
	ciclista=models.ForeignKey(Ciclista)
	precio = models.IntegerField()

	def __unicode__(self):
		return unicode(self.precio)


class Envio(models.Model):
	"""
		Clase que representa una oferta aceptada
	"""
	TIPOS_ESTADOS=(
		('esperando', 'esperando'),
		('enviando', 'enviando'),
		('entregado', 'entregado'),
	)

	estado=models.CharField(max_length=50, choices=TIPOS_ESTADOS, default='esperando')
	oferta=models.ForeignKey(Oferta)
	anuncio=models.ForeignKey(Anuncio)

