from envios.models import Anuncio, Oferta, Envio
from rest_framework import serializers


class AnuncioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anuncio
        fields = ('pk', 'remitente','descripcion','telefonoRemitente','telefonoReceptor','nombreRemitente','nombreReceptor','direccionRemitente','datosAdicionalesDireccionReceptor','datosAdicionalesDireccionRemitente','direccionReceptor','latitudPuntoInicial','longitudPuntoInicial', 'latitudPuntoFinal', 'longitudPuntoFinal')
        #fields = "__all__"

class OfertaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Oferta
		fields = ('pk','anuncio', 'ciclista', 'precio')

class EnvioSerializer(serializers.ModelSerializer):

	class Meta:
		model = Envio
		fields = ('pk', 'estado', 'oferta', 'anuncio')

