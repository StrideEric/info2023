from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.Home_Noticias, name='home_noticias'),
    
    path('crear_noticia', views.Crear_Noticia.as_view(), name='crear_noticia'),

#    # Noticias
#    path('noticia/<int:id_noticia>', views.Noticia, name='noticia'),
#    path('categoria/<int:id_categoria>', views.Categoria, name='categoria'),
#    path('buscar', views.Buscar, name='buscar'),
#    path('editar_noticia/<int:id_noticia>', views.Editar_Noticia, name='editar_noticia'),
#    path('eliminar_noticia/<int:id_noticia>', views.Eliminar_Noticia, name='eliminar_noticia'),
#    # Categorias
#    path('crear_categoria', views.Crear_Categoria, name='crear_categoria'),
#    path('editar_categoria/<int:id_categoria>', views.Editar_Categoria, name='editar_categoria'),
#    path('eliminar_categoria/<int:id_categoria>', views.Eliminar_Categoria, name='eliminar_categoria'),
#    # Comentarios
#    path('crear_comentario/<int:id_noticia>', views.Crear_Comentario, name='crear_comentario'),
#    path('editar_comentario/<int:id_comentario>', views.Editar_Comentario, name='editar_comentario'),
#    path('eliminar_comentario/<int:id_comentario>', views.Eliminar_Comentario, name='eliminar_comentario'),
]
