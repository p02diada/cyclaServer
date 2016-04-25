from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from usuarios import views

urlpatterns = [
#    url(r'^list/$', views.usuarios_list),
#    url(r'^user/(?P<pk>[0-9]+)/$', views.usuarios_detail),
     url(r'^registrarCiclista/$', views.registrarCiclista),
     url(r'^registrarRemitente/$', views.registrarRemitente),
     url(r'^getTipoUsuario/(?P<username>\w+)/$', views.getTipoUsuario),
     url(r'^getIdUsuario/(?P<username>\w+)/$', views.getIdUsuario),
     url(r'^getDatosCiclistaPorId/$', views.getDatosCiclistaPorId),
     #url(r'^dameUsuario/$', views.dameUsuario),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)