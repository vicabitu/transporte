from django.db import models

class Parada(models.Model):
    """
        Representa una parada de un recorrido.
    """
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)

class PuntoDeCarga(models.Model):
    """
        Puntos donde uno puede recargar su tarjeta Sube.
    """
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)

class Recorrido(models.Model):
    """
        Recorrido de una linea de la empresa.
    """
    numero_linea = models.IntegerField()
    color = models.CharField(max_length=10)
    ruta = models.ManyToManyField(Parada)
"""
class Mapa(models.Model):

    posicion_inicial = Coordenada

    def __init__(self, posicion_inicial, zoom):
        self.posicion_inicial = posicion_inicial
        self.zoom = zoom

class Marcador(models.Model):

    def __init__(self, posicion, mapa):
        self.posicion = posicion
        self.mapa = mapa
"""