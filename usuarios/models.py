from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Remitente(User):
     
    """
        Clase que representa a los usuarios que van a publicar envios del sistema.
        Atributos heredados de User y que vamos a usar:
            username: nombre de usuario
            password: password del usuario
            email: direccion de correo
    """

    def __unicode__(self):
        return self.username


class Ciclista(User):
     
    """
        Clase que representa a los usuario que van a transportar los paquetes.
        Atributos heredados de User y que vamos a usar:
            username: nombre de usuario
            password: password del usuario
            email: direccion de correo
    """

    valoracionMedia= models.IntegerField()

    def __unicode__(self):
        return self.username