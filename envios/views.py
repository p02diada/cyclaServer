from django.shortcuts import render
from envios.models import Anuncio, Oferta, Envio
from rest_framework import viewsets
from envios.serializers import AnuncioSerializer, OfertaSerializer, EnvioSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import math
# Create your views here.


@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def crearAnuncio(request):

    """
    Vista que nos permite crear un nuevo Anuncio.
    """
    #ciclista = Ciclista.objects.get(username=request.user)

    print request.user
    print "dentrooooo"
    if request.method == 'POST':
    	print "dentro del iff"
        serializer = AnuncioSerializer(data=request.data)
        print serializer       
        if serializer.is_valid():

            print "serializer valido"
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
@api_view(['POST','PUT', 'GET'])
def getAnuncios(request):
	latitudeActual=request.POST.get('latitude','')
	longitudeActual=request.POST.get('longitude','')

	print "latitudeActual: "+ latitudeActual
	print "longitudeActual: "+ longitudeActual

	latitudActual=float(latitudeActual)
	longitudActual=float(longitudeActual)



	anuncios=Anuncio.objects.all()

	for anuncio in anuncios:
		latitud=anuncio.latitudPuntoFinal
		longitud=anuncio.longitudPuntoInicial

		print "latitud: " + latitud
		print "longitud: " + longitud

		latitud=float(latitud)
		longitud=float(longitud)
		metrosLongitudPuntoA=longitud*(10000000/90)
		print metrosLongitudPuntoA
		metrosLatitudPuntoA=latitud*(40000000/360)
		print metrosLatitudPuntoA

		metrosLongitudActual=longitudActual*(10000000/90)
		print metrosLongitudActual
		metrosLatitudActual=latitudActual*(40000000/360)
		print metrosLatitudActual

		diferenciaLongitudMetros=metrosLongitudPuntoA-metrosLongitudActual
		print diferenciaLongitudMetros
		diferenciaLatitudMetros=metrosLatitudPuntoA-metrosLatitudActual
		print diferenciaLatitudMetros

		diferenciaLongitudMetros=diferenciaLongitudMetros*diferenciaLongitudMetros
		diferenciaLatitudMetros=diferenciaLatitudMetros*diferenciaLatitudMetros

		sumaMetros=diferenciaLatitudMetros+diferenciaLongitudMetros

		distacia=math.sqrt(sumaMetros)
		print "distancia: "
		print distacia







	serializer=AnuncioSerializer(anuncios, many=True)
	return Response(serializer.data)

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

