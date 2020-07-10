from django.contrib import admin

# Register your models here.
from .models import *
# from colexin.models import *



class ColexinAdmin(admin.ModelAdmin):
    list_display = itemColexin
    list_display_links = itemColexin

class ContactoAdmin(admin.ModelAdmin):
    list_display = itemContacto
    list_display_links = itemContacto

class RedesAdmin(admin.ModelAdmin):
    list_display = itemRedes
    list_display_links = itemRedes


admin.site.register(Colexin,ColexinAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Redes,RedesAdmin)