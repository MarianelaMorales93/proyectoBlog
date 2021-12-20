from django.db import models

# Create your models here.
#hola

class Post(models.Model):
    categoria=models.CharField(max_length=30)
    fecha_publicacion=models.DateField()
    