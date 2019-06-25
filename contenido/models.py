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
	image = models.ImageField(upload_to='img/galeria', null=True)
	titulo = models.CharField(max_length = 100, null=True)
	comentario = models.TextField(help_text='comentario de la foto',null=True)
	fecha_creacion = models.DateField(null=True)

	class Meta:
		verbose_name = "Galeria"
		verbose_name_plural = "Galerias"

	def __str__(self):
		return "%s" %(self.titulo)

class AboutMe(models.Model):
	image = models.ImageField(upload_to='img/about-me', null=True)
	pregunta = models.CharField(max_length=1000)
	respuesta = models.TextField(help_text='respuesta de la pregunta')

	class Meta:
		verbose_name = "About"
		verbose_name_plural = "Abouts"

	def __str__(self):
		return "%s" %(self.pregunta)




class Proyecto(models.Model):
	image = models.ImageField(upload_to='img/proyecto')
	nombre = models.CharField(max_length=100)
	nuevo = models.BooleanField(default=True)
	descripcion = models.TextField(help_text='descripción corta del proyecto')
	url = models.URLField(blank=True, null=True, help_text='Página web del proyecto.')

	class Meta:
		verbose_name = "Proyecto"
		verbose_name_plural = "Proyectos"

	def __str__(self):
		return "%s" %(self.nombre)



class Caracteristica(models.Model):
	caracteristica = models.CharField(max_length = 100)
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='caracteristica_proyecto', null=True)


	class Meta:
		verbose_name = "Caracteristica"
		verbose_name_plural = "Caracteristicas"

		def __str__(self):
			return "%s" %(self.nombre)
