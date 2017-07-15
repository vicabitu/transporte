from django.shortcuts import render
from recorrido.models import *

def mostrar(request):


    contexto = {
        "marcadores": Marcador.objects.all().first()
    }
    print(contexto)
    return render(request, 'recorrido/mapa.html', contexto)

