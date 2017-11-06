from django.conf.urls import include, url

from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^estudiantes/nuevo/$', views.estudiante_nuevo, name='estudiante_nuevo'),
    url(r'^estudiantes/(?P<pk>[0-9]+)/editar/$', views.estudiante_editar, name='estudiante_editar'),
    url(r'^estudiantes/list/$', views.estudiante_list, name='estudiante_list'),
    url(r'^estudiantes/(?P<pk>[0-9]+)/eliminar/$', views.estudiante_eliminar, name='estudiante_eliminar'),
    url(r'^estudiantes/(?P<pk>[0-9]+)/ver/$', views.estudiante_ver, name='estudiante_ver'),

    url(r'^cursos/nuevo/$', views.curso_nuevo, name='curso_nuevo'),
    url(r'^cursos/(?P<pk>[0-9]+)/editar/$', views.curso_editar, name='curso_editar'),
    url(r'^cursos/list/$', views.cursos_list, name='cursos_list'),
    url(r'^cursos/(?P<pk>[0-9]+)/eliminar/$', views.curso_eliminar, name='curso_eliminar'),
    url(r'^cursos/(?P<pk>[0-9]+)/ver/$', views.curso_ver, name='curso_ver'),

    url(r'^profesores/nuevo/$', views.profesor_nuevo, name='profesor_nuevo'),
    url(r'^profesores/(?P<pk>[0-9]+)/editar/$', views.profesor_editar, name='profesor_editar'),
    url(r'^profesores/(?P<pk>[0-9]+)/eliminar/$', views.profesor_eliminar, name='profesor_eliminar'),
    url(r'^profesores/(?P<pk>[0-9]+)/ver/$', views.profesor_ver, name='profesor_ver'),
    url(r'^profesores/list/$', views.profesor_list, name='profesor_list'),

    url(r'^aula/nuevo/$', views.aula_nuevo, name='aula_nuevo'),
    url(r'^aula/(?P<pk>[0-9]+)/editar/$', views.aula_editar, name='aula_editar'),
    url(r'^aula/list/$', views.aula_list, name='aula_list'),
    url(r'^aula/(?P<pk>[0-9]+)/eliminar/$', views.aula_eliminar, name='aula_eliminar'),
    url(r'^aula/(?P<pk>[0-9]+)/ver/$', views.aula_ver, name='aula_ver'),
]
