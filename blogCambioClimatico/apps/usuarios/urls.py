from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.Perfil, name='perfil'),

#    path('login', views.Login, name='login'),
#    path('logout', views.Logout, name='logout'),
##    path('registro', views.Registro, name='registro'),
#    path('editar_perfil', views.Editar_Perfil, name='editar_perfil'),
#    path('eliminar_perfil', views.Eliminar_Perfil, name='eliminar_perfil'),
#    path('cambiar_contrasena', views.Cambiar_Contrasena, name='cambiar_contrasena'),
#    path('recuperar_contrasena', views.Recuperar_Contrasena, name='recuperar_contrasena'),
#    path('editar_foto_perfil', views.Editar_Foto_Perfil, name='editar_foto_perfil'),


]
