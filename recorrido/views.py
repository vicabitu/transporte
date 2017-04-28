from django.shortcuts import render

def mostrar(request):

    return render(request, 'recorrido/mapa.html', {})