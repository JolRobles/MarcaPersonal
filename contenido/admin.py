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
