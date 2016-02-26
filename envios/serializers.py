from envios.models import Anuncio, Oferta, Envio
from rest_framework import serializers


class AnuncioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anuncio
        fields = ('remitente','descripcion','latitudPuntoInicial','longitudPuntoInicial', 'latitudPuntoFinal', 'longitudPuntoFinal')
        #fields = "__all__"

class OfertaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Oferta
		fields = "__all__"

class EnvioSerializer(serializers.ModelSerializer):

	class Meta:
		model = Envio
		fields = "__all__"

