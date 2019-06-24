from django.contrib import admin

# Register your models here.

from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class PortadaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'video')

admin.site.register(Portada, PortadaAdmin)


class SeccionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'icono', 'nombre', 'titulo', 'subtitulo')

admin.site.register(Seccion, SeccionAdmin)
