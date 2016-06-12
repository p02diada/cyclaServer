from django.shortcuts import render
from envios.models import Anuncio, Oferta, Envio
from rest_framework import viewsets
from envios.serializers import AnuncioSerializer, OfertaSerializer, EnvioSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from usuarios.models import Ciclista, Remitente
from usuarios.serializers import CiclistaSerializer
from django.core import serializers
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



	anuncios=Anuncio.objects.filter(estado='activo')
	lista_anuncios=[]
	lista_distancias=[]

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

		distancia=math.sqrt(sumaMetros)
		print "distancia: "
		print distancia
		if distancia<20000:
			lista_anuncios.append(anuncio)
			lista_distancias.append(distancia)








	serializer=AnuncioSerializer(anuncios, many=True)
	return Response(serializer.data)


@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getMisAnuncios(request):

	id_usuario=request.POST.get('id_usuario','')
	anuncios=Anuncio.objects.filter(remitente=id_usuario, estado='activo')
	serializer=AnuncioSerializer(anuncios, many=True)
	return Response(serializer.data)

@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getOfertasParaAnuncio(request):
	listaDatosCiclista=[]
	id_anuncio=request.POST.get('id_anuncio','')
	ofertas=Oferta.objects.filter(anuncio=id_anuncio)
	for oferta in ofertas:
		print oferta
		print oferta.ciclista
		datosCiclista=Ciclista.objects.get(pk=oferta.ciclista)
		print datosCiclista.pk
		print datosCiclista.valoracionMedia
		listaDatosCiclista.append(datosCiclista)

	print listaDatosCiclista
	serializerCiclista=CiclistaSerializer(listaDatosCiclista, many=True)
	serializerOferta=OfertaSerializer(ofertas, many=True)
	content={
		'listaOfertas': serializerOferta.data,
		'listaDatosCiclista': serializerCiclista.data

	}
	return Response(content)

	
@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def crearOferta(request):

    """
    Vista que nos permite crear un nuevo Anuncio.
    """
    #ciclista = Ciclista.objects.get(username=request.user)

    print request.user
    print "dentrooooo"
    if request.method == 'POST':
    	print "dentro del iff"
        serializer = OfertaSerializer(data=request.data)
        print serializer       
        if serializer.is_valid():

            print "serializer valido"
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def aceptarOferta(request):
	id_anuncio=request.POST.get('id_anuncio','')
	id_oferta=request.POST.get('id_oferta','')
	anuncio=Anuncio.objects.get(pk=id_anuncio)
	oferta=Oferta.objects.get(pk=id_oferta)
	print oferta
	Oferta.objects.filter(anuncio=id_anuncio).exclude(pk=id_oferta).delete()
	anuncio.estado='caducado'
	anuncio.save()
	envio= Envio.objects.create(oferta=oferta, anuncio=anuncio)
	print envio.estado
	print envio.oferta
	print envio.anuncio
	content={
		'envio': "ok",
		

	}
	return Response(content)

@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getEnviosRemitente(request):
	id_usuario=request.POST.get('id_usuario','')
	listaAnuncios=[]
	
	anuncios=Anuncio.objects.filter(estado='caducado').filter(remitente=id_usuario)

	envios=Envio.objects.filter(anuncio=anuncios)

	listaEnvios=EnvioSerializer(envios, many=True)

	listaAnuncios=AnuncioSerializer(anuncios, many=True)

	content={
		'listaEnvios': listaEnvios.data,
		'listaAnuncios': listaAnuncios.data,
	}
	return Response(content)

@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getEnviosCiclista(request):
	id_usuario=request.POST.get('id_usuario','')

	ofertas=Oferta.objects.filter(ciclista=id_usuario)

	envios=Envio.objects.filter(oferta=ofertas)

	if envios:
		anuncio=Anuncio.objects.get(pk=envios[0].anuncio.pk)
		oferta=Oferta.objects.get(pk=envios[0].oferta.pk)

		envioSer=EnvioSerializer(envios[0])
		anuncioSer=AnuncioSerializer(anuncio)
		ofertaSer=OfertaSerializer(oferta)



		content={
			'envio':envioSer.data,
			'anuncio':anuncioSer.data,
			'oferta':ofertaSer.data,
		}
		return Response(content)
	else:
		content={
			'respuesta':'No hay envios',
		}
		return Response(content)


@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getAnuncioPorId(request):
	id_anuncio=request.POST.get('id_anuncio','')
	anuncio=Anuncio.objects.get(pk=id_anuncio)
	print anuncio
	anuncio=AnuncioSerializer(anuncio)
	print anuncio.data
	content={
		'anuncio':anuncio.data
	}
	return Response(content)

@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getOfertaPorId(request):
	id_oferta=request.POST.get('id_oferta','')
	oferta=Oferta.objects.get(pk=id_oferta)
	print oferta
	oferta=OfertaSerializer(oferta)
	print oferta.data
	content={
		'oferta':oferta.data
	}
	return Response(content)		

@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getPosicionCiclistaPorId(request):
	id_ciclista=request.POST.get('id_ciclista','')
	ciclista=Ciclista.objects.get(pk=id_ciclista)
	print ciclista.latitudUltimoPunto
	content={
		'longitudCiclista':ciclista.longitudUltimoPunto,
		'latitudCiclista':ciclista.latitudUltimoPunto,
	}
	return Response(content)

@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def cambiarEstadoEnvio(request):
	print 'HOLAAAAAAAAAAAAAA'
	estado=request.POST.get('estado','')
	id_envio=request.POST.get('id_envio','')
	envio=Envio.objects.get(pk=id_envio)
	envio.estado=estado
	envio.save()
	content={
		'Ok': 'Ok'
	}
	return Response(content)

@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def cambiarValoracionCiclista(request):
	id_ciclista=request.POST.get('id_ciclista','')
	valoracion=request.POST.get('valoracion','')
	ciclista=Ciclista.objects.get(pk=id_ciclista)
	valoracionMedia=ciclista.valoracionMedia
	valoracion=int(valoracion)
	valoracionFinal=(valoracionMedia+valoracion)/(ciclista.cantidadValoraciones + 1)
	ciclista.valoracionMedia=valoracionFinal
	ciclista.cantidadValoraciones=ciclista.cantidadValoraciones+1
	ciclista.save()
	content={
		'Ok': 'Ok'
	}
	return Response(content)

@api_view(['POST','PUT', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def borrarAnuncio(request):
	id_anuncio=request.POST.get('id_anuncio','')
	anuncio=Anuncio.objects.get(pk=id_anuncio)
	respuesta=anuncio.delete()
	print respuesta
	content={
		'Ok': 'Ok'
	}
	return Response(content)


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

