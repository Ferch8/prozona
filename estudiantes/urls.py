from django.conf.urls import include, url

from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^estudiante/nuevo/$', views.estudiante_nuevo, name='estudiante_nuevo'),
]
