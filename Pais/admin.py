from django.contrib import admin

# Register your models here.
from Pais.models import *


class ContinenteAdmin(admin.ModelAdmin):
    list_display = itemContinente
    list_display_links = itemContinente

class PaisAdmin(admin.ModelAdmin):
    list_display = itemPais
    list_display_links = itemPais

class AniosAdmin(admin.ModelAdmin):
    list_display = itemAnios
    list_display_links = itemAnios

class PeriodoAdmin(admin.ModelAdmin):
    list_display = itemPeriodo
    list_display_links = itemPeriodo

class Sistema_monetarioAdmin(admin.ModelAdmin):
    list_display = itemSistema_monetario
    list_display_links = itemSistema_monetario

class MotivoAdmin(admin.ModelAdmin):
    list_display = itemMotivo
    list_display_links = itemMotivo


class DenominacionAdmin(admin.ModelAdmin):
    list_display = itemDeniminacion
    list_display_links = itemDeniminacion

class Denimina_detalleAdmin(admin.ModelAdmin):
    list_display = itemDenimina_detalle
    list_display_links = itemDenimina_detalle

class CecasAdmin(admin.ModelAdmin):
    list_display = itemCecas
    list_display_links = itemCecas

class AleacionAdmin(admin.ModelAdmin):
    list_display = itemAleacion
    list_display_links = itemAleacion



admin.site.register(Continente,ContinenteAdmin)
admin.site.register(Anios,AniosAdmin)
admin.site.register(Pais,PaisAdmin)
admin.site.register(Periodo,PeriodoAdmin)
admin.site.register(Motivo,MotivoAdmin)
admin.site.register(Sistema_monetario,Sistema_monetarioAdmin)
admin.site.register(Denominacion,DenominacionAdmin)
admin.site.register(Denimina_detalle,Denimina_detalleAdmin)
admin.site.register(Cecas,CecasAdmin)
admin.site.register(Aleacion,AleacionAdmin)