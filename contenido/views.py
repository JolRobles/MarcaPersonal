from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *
from .forms import *

class BlogDetail(DetailView):
	model = Blog
	form_class = BlogForm
	# success_url = reverse_lazy('index:suscripcion_list')
