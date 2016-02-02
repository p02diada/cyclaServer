from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from usuarios.models import Ciclista, Remitente 
from usuarios.serializers import CiclistaSerializer, RemitenteSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class CiclistaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ciclista.objects.all().order_by('-date_joined')
    serializer_class = CiclistaSerializer


class RemitenteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Remitente.objects.all()
    serializer_class = RemitenteSerializer


