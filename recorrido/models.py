from django.db import models

"""
class Coordenada(models.Model):

    latitud = models.IntegerField
    longitud = models.IntegerField

    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud


class Mapa(models.Model):

    posicion_inicial = Coordenada

    def __init__(self, posicion_inicial, zoom):
        self.posicion_inicial = posicion_inicial
        self.zoom = zoom


class Marcador(models.Model):

    def __init__(self, posicion, mapa):
        self.posicion = posicion
        self.mapa = mapa


class Recorrido(models.Model):

    def __init__(self, ruta, mapa, color):
        self.ruta = ruta    #arreglo de objetos coordenada
        self.mapa = mapa
        self.color = color
"""