from django.shortcuts import render, redirect
from .models import *
from contenido.models import Blog, Galeria

# Create your views here.
def index(request):
	blogs = Blog.objects.all()
	imagenes = Galeria.objects.all()
	context = {
		'blogs':blogs,
		'imagenes':imagenes,

	}
	return render(request, 'index.html', context)

# Carga de landing page presentacion
def landing_page(request):
    configuracion = Configuracion.objects.first()
    titulo = configuracion.titulo_landing_page
    descripcion = configuracion.descripcion_landing_page
    texto_testimonios = configuracion.texto_testimonios
    texto_nuestros_clientes = configuracion.texto_nuestros_clientes
    secciones = Seccion.objects.all()
    testimonios = Testimonio.objects.all()
    context = {
        'titulo':titulo,
        'descripcion':descripcion,
        'texto_testimonios':texto_testimonios,
        'texto_nuestros_clientes':texto_nuestros_clientes,
        'secciones':secciones,
        'testimonios':testimonios,
    }
    return render(request, 'landing_page/index.html', context)
