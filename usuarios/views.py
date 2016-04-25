from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from usuarios.models import Ciclista, Remitente 
from usuarios.serializers import CiclistaSerializer, RemitenteSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status


#for user in User.objects.all():
#    Token.objects.get_or_create(user=user)

#Crea tokens para los usuarios nuevos
#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    print "EEEEEEEEEEEEEEEE"
#    if created:
#        Token.objects.create(user=instance)

@api_view(['POST','PUT'])
#@authentication_classes((TokenAuthentication,))
#@permission_classes((IsAuthenticated,))
def registrarCiclista(request):

    """
    Vista que nos permite crear un nuevo Ciclista.
    """


    #ciclista = Ciclista.objects.get(username=request.user)

    print request.user
    if request.method == 'POST':
        serializer = CiclistaSerializer(data=request.data)
        print serializer       
        if serializer.is_valid():
            #Para crear el token del nuevo ciclista
            guardado=serializer.save()
            usuario=User.objects.get(username=guardado)
            #no se activaba por defecto
            usuario.is_active=True
            usuario.save()
            #Para crear el token del nuevo ciclista
            token=Token.objects.create(user=usuario)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','PUT'])
def registrarRemitente(request):

    """
    Vista que nos permite crear un nuevo Remitente.
    """
    if request.method == 'POST':
        serializer = RemitenteSerializer(data=request.data)
        if serializer.is_valid():
            #Para crear el token del nuevo remitente
            guardado=serializer.save()
            usuario=User.objects.get(username=guardado)
            #no se activaba por defecto
            usuario.is_active=True
            usuario.save()
            #User.objects.get(username=guardado).update(is_active=True)
            token=Token.objects.create(user=usuario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getTipoUsuario(request, username):

    try:
        remitente=Remitente.objects.get(username=username)
    except Remitente.DoesNotExist:
        remitente=None

    if remitente:
        content = {
            'esRemitente': True
        }
        return Response(content)
    else:
        content = {
            'esRemitente': False
        }
        return Response(content)

@api_view(['GET'])
def getIdUsuario(request, username):

    try:
        usuario=Remitente.objects.get(username=username)
    except Remitente.DoesNotExist:
        usuario=Ciclista.objects.get(username=username)
   
    content = {
       'id_usuario': usuario.pk
    }
    return Response(content)

@api_view(['POST'])
def getDatosCiclistaPorId(request):

    id_ciclista=request.POST.get('id_ciclista','')
    ciclista=Ciclista.objects.get(pk=id_ciclista)
    print ciclista
    content={
        'username':ciclista.username,
        'valoracionMedia':ciclista.valoracionMedia
    }
    return Response(content)




class UserViewSet(viewsets.ModelViewSet):

    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    queryset=User.objects.all()
    serializer_class=UserSerializer

class RemitenteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Remitente.objects.all()
    serializer_class = RemitenteSerializer


