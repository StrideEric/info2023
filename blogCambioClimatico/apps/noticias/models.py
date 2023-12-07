from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_creado = models.DateTimeField(
        'creado',
        auto_now_add=True
        )
    fecha_actualizado = models.DateTimeField(
        'actualizado',
        auto_now=True
        )

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='noticias')
    fecha_creado = models.DateTimeField(
        'creado',
        auto_now_add=True
        )
    fecha_actualizado = models.DateTimeField(
        'actualizado',
        auto_now=True
        )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) #siempre que tenemos foreign key, tenemos que importar el modelo


    def __str__(self):
        return self.titulo
    