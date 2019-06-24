from django.db import models

# Create your models here.
class Blog(models.Model):
	image = models.ImageField(upload_to='img/blog')
	titulo = models.CharField(max_length = 100)
	contenido = models.TextField(help_text='Contenido del blog')
	fecha_creacion = models.DateField(null=True)

	class Meta:
		verbose_name = "Blog"
		verbose_name_plural = "Blogs"

	def __str__(self):
		return "%s" %(self.titulo)

class Galeria(models.Model):
	image = models.ImageField(upload_to='img/galeria')
	titulo = models.CharField(max_length = 100, null=True)
	comentario = models.TextField(help_text='comentario dela foto',null=True)
	fecha_creacion = models.DateField(null=True)
