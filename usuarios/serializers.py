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
        fields = ('username', 'password', 'email', 'is_active', 'date_joined', 'valoracionMedia')
        extra_kwargs = {
                 'password': {'write_only': True}
         }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class RemitenteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Remitente
        fields = ('username', 'password', 'email', 'is_active', 'date_joined')
        extra_kwargs = {
                 'password': {'write_only': True}
         }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

