__author__ = 'manuel'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^contacto$', views.contacto, name='contacto'),
    url(r'^iner$', views.iner, name='iner'),
    url(r'^mostrarDatos$', views.mostrarDatos, name='mostrarDatos'),
    url(r'^cargarDatos$', views.cargarDatos, name='cargarDatos'),
    url(r'^temperaturaJson', views.temperaturaJson, name='temperaturaJson'),
    url(r'^humedadJson', views.humedadJson, name='humedadJson'),
    url(r'^viento', views.vientoJson, name='vientoJson'),
    url(r'^presionBarometricaJson', views.presionBarometricaJson, name='presionBarometricaJson'),
    url(r'^reporte', views.reporteGeneral, name='reporte'),
    url(r'^estacionesCampos', views.estacionesCampos, name='estacionesCampos'),
    url(r'^graficaCampos', views.graficaCampos, name='graficaCampos'),



]