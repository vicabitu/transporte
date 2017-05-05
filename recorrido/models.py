from django.db import models

class Coordenada(models.Model):
    """
    Representa una coordenada en el mapa
    """

    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)


class Mapa(models.Model):
    """
    Representa el mapa de la ciudad en donde van a estar los dintintos recorridos y marcadores
    """

    posicion_inicial = models.OneToOneField(Coordenada)
    zoom = models.IntegerField()


class Marcador(models.Model):
    """
    Represemta un marcador dentro del mapa, puede ser una parada de colectivo, un punto de venta,
    lugar de informacion, etc
    """

    posicion = models.OneToOneField(Coordenada)
    icono = models.CharField(max_length=100)
    mapa = models.OneToOneField(Mapa, null=True)
    tipo = models.CharField(max_length=30)


class Recorrido(models.Model):
    """
    Representa un recorrido en el mapa
    """
    nombre = models.CharField(max_length=10)
    cordenada = models.ManyToManyField(Coordenada)
    color = models.CharField(max_length=10)
    mapa = models.OneToOneField(Mapa, null=True)
    ancho = models.IntegerField()



