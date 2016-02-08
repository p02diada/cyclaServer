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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#for user in User.objects.all():
#    Token.objects.get_or_create(user=user)

#Crea tokens para los usuarios nuevos
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@api_view(['POST','PUT'])
def registrarCiclista(request):

    """
    Vista que nos permite crear un nuevo usuario.
    """


    #ciclista = Ciclista.objects.get(username=request.user)

    print request.user
    if request.method == 'POST':
        serializer = CiclistaSerializer(data=request.data)
        print serializer       
        if serializer.is_valid():
            serializer.save()
            #print guardado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','PUT'])
def registrarRemitente(request):

    """
    Vista que nos permite crear un nuevo usuario.
    """


    #ciclista = Ciclista.objects.get(username=request.user)

    print request.user
    if request.method == 'POST':
        serializer = RemitenteSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


