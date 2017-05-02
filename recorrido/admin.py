from django.contrib import admin
from recorrido.models import *

class ParadaAdmin(admin.ModelAdmin):
    pass

class PuntoDeCargaAdmin(admin.ModelAdmin):
    pass

class RecorridoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Parada, ParadaAdmin)
admin.site.register(PuntoDeCarga, PuntoDeCargaAdmin)
admin.site.register(Recorrido, RecorridoAdmin)