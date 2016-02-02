from django.shortcuts import render
from envios.models import Anuncio, Oferta, Envio
from rest_framework import viewsets
from envios.serializers import AnuncioSerializer, OfertaSerializer, EnvioSerializer
# Create your views here.

class AnuncioViewSet (viewsets.ModelViewSet):
	"""
		Clase que obtiene todos los Anuncios
	"""
	queryset = Anuncio.objects.all()
	serializer_class=AnuncioSerializer


class OfertaViewSet (viewsets.ModelViewSet):
	"""
		Clase que obtiene todos los Anuncios
	"""
	queryset = Oferta.objects.all()
	serializer_class=OfertaSerializer

class EnvioViewSet (viewsets.ModelViewSet):
	"""
		Clase que obtiene todos los Anuncios
	"""
	queryset = Envio.objects.all()
	serializer_class=EnvioSerializer

