from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.views.generic.edit import CreateView
from .forms import ComicForm


from .models import Comic
# from .forms import ComicForm

# Create your views here.
class TableView(TemplateView):
	template_name = 'e-commerce/tabla.html'

class ListaView(TemplateView):
	template_name = 'e-commerce/lista.html'

class FormularioView(TemplateView):
	template_name = 'e-commerce/formulario.html'

class TextoView(TemplateView):
	template_name = 'e-commerce/texto.html'

class ImagenView(TemplateView):
	template_name = 'e-commerce/imagen.html'


#Insertar comic a la base de datos
class AgregarComicView(CreateView):
	model = Comic
	template_name = 'e-commerce/agregar-comic.html'
	form_class = ComicForm

