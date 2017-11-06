from django.conf.urls import include, url

from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^estudiantes/nuevo/$', views.estudiante_nuevo, name='estudiante_nuevo'),
    url(r'^estudiantes/(?P<pk>[0-9]+)/editar/$', views.estudiante_editar, name='estudiante_editar'),
    url(r'^cursos/nuevo/$', views.curso_nuevo),
    url(r'^cursos/(?P<pk>[0-9]+)/editar/$', views.curso_editar, name='curso_editar'),
    url(r'^profesores/nuevo/$', views.profesor_nuevo),
    url(r'^profesores/(?P<pk>[0-9]+)/editar/$', views.profesor_editar, name='profesor_editar'),
    url(r'^aula/nuevo/$', views.aula_nuevo),
    url(r'^aula/(?P<pk>[0-9]+)/editar/$', views.aula_editar, name='aula_editar'),
    url(r'^cursos/list/$', views.cursos_list, name='cursos_list'),
]
