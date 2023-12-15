from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Home, name ='inicio'),
    path('contacto', views.Contacto, name ='contacto'),
    path('nosotros', views.Nosotros, name ='nosotros'),

    #APP NOTICIAS
    path('noticias/', include('apps.noticias.urls')),

    #APP USUARIOs
    path('Usuarios/', include('apps.usuarios.urls')),

    #APP COMENTARIOS
    path('Comentarios/', include('apps.comentarios.urls')),


    #LOGIN Y LOGOUT
    path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth.LogoutView.as_view(),name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
