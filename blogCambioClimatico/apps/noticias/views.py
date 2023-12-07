from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Noticia
from .forms import Formulario_Noticia

def Home_Noticias(request):

    all = Noticia.objects.all()

    dict = {} #Diccionario, pasa cada elemento del objetcts en la variable all a la variable noticias

    dict['noticias'] = all


    return render(request, 'noticias/home_noticias.html', dict)


class Crear_Noticia(CreateView):
    model = Noticia
    template_name = 'noticias/crear_noticia.html'
    form_class = Formulario_Noticia
    success_url = reverse_lazy('noticias:home_noticias')