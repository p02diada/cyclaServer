from django.contrib.auth.models import User, Group
from rest_framework import serializers
from usuarios.models import Ciclista, Remitente

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields = ('url', 'username', 'email')

class CiclistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ciclista
        fields = "__all__"

class RemitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remitente
        fields = "__all__"


