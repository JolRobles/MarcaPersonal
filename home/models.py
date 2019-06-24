from django.db import models


class Portada(models.Model):
	video = models.FileField(upload_to='videos/')

	class Meta:
		verbose_name = "Portada"
		verbose_name_plural = "Portadas"


class Seccion(models.Model):
	icono = models.ImageField(upload_to='img')
	nombre = models.CharField(max_length = 50)
	titulo = models.CharField(max_length = 200)
	subtitulo = models.CharField(max_length = 200)

	class Meta:
		verbose_name = "Seccion"
		verbose_name_plural = "Secciones"

	def __str__(self):
		return "%s" %(self.nombre)
