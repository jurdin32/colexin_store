from django.contrib import admin

# Register your models here.
from .models import *

# class ProductAdmin(admin.ModelAdmin):
#     fields = ('image','title','price','descripcion')
#     list_display = ('__str__','slug')



class ProductAdminn(admin.ModelAdmin):
    list_display = itemProduct
    list_display_links = itemProduct

class Tipo_ProductoAdmin(admin.ModelAdmin):
    list_display = itemTipo_Producto
    list_display_links = itemTipo_Producto


class MonedaAdmin(admin.ModelAdmin):
    list_display = itemMoneda
    list_display_links = itemMoneda

class BilleteAdmin(admin.ModelAdmin):
    list_display = itemBillete
    list_display_links = itemBillete


# admin.site.register(Product,ProductAdmin)
admin.site.register(Tipo_Producto,Tipo_ProductoAdmin)
admin.site.register(Product,ProductAdminn)
admin.site.register(Moneda,MonedaAdmin)
admin.site.register(Billete,BilleteAdmin)