from django.contrib import admin

# Register your models here.
from Blogs.models import *


class CategoriaAdmin(admin.ModelAdmin):
    list_display = itemCategoria
    list_display_links = itemCategoria


class BlogsAdmin(admin.ModelAdmin):
    list_display = itemBlogs
    list_display_links = itemBlogs


# class BlogVisitaAdmin(admin.ModelAdmin):
#     list_display = itemVisitas_Blog
#     list_display_links = itemVisitas_Blog



# class ComentarioAdmin(admin.ModelAdmin):
#     list_display = itemComentario
#     list_display_links = itemComentario
#
#
# class RespuestaAdmin(admin.ModelAdmin):
#     list_display = itemRespuesta
#     list_display_links = itemRespuesta


admin.site.register(Blogs,BlogsAdmin)
# admin.site.register(Visitas_Blog,BlogVisitaAdmin)
admin.site.register(Categoria,CategoriaAdmin)
# admin.site.register(Comentario,ComentarioAdmin)
# admin.site.register(Respuesta)