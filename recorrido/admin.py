from django.contrib import admin
from recorrido.models import *

class CoordenadaAdmin(admin.ModelAdmin):
    pass
class MapaAdmin(admin.ModelAdmin):
    pass

class MarcadorAdmin(admin.ModelAdmin):
    pass

class RecorridoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Coordenada, CoordenadaAdmin)
admin.site.register(Mapa, MapaAdmin)
admin.site.register(Marcador, MarcadorAdmin)
admin.site.register(Recorrido, RecorridoAdmin)