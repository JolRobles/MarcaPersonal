from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'image', 'titulo', 'contenido', 'fecha_creacion')

admin.site.register(Blog, BlogAdmin)

class GaleriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'image', 'titulo', 'comentario', 'fecha_creacion')

admin.site.register(Galeria, GaleriaAdmin)


class AboutMeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'image', 'pregunta', 'respuesta')

admin.site.register(AboutMe, AboutMeAdmin)

class ProyectoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'image', 'nombre', 'nuevo', 'descripcion')

admin.site.register(Proyecto, ProyectoAdmin)

class CaracteristicaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'caracteristica', 'proyecto')

admin.site.register(Caracteristica, CaracteristicaAdmin)
