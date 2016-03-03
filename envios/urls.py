from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from envios.models import Anuncio
from envios import views

urlpatterns = [
#    url(r'^list/$', views.usuarios_list),
#    url(r'^user/(?P<pk>[0-9]+)/$', views.usuarios_detail),
     url(r'^crearAnuncio/$', views.crearAnuncio),
     url(r'^getAnuncios/$', views.getAnuncios),

     #url(r'^registrarRemitente/$', views.registrarRemitente),
     #url(r'^dameUsuario/$', views.dameUsuario),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)