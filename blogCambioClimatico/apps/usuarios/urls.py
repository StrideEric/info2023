
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
  	path('Registro/', views.Registro.as_view(), name="registro_usuario"),
	path('Perfil/', views.Perfil.as_view(), name="perfil"),

]
