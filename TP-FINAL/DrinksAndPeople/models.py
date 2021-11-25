from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    id_IngredientCocktailDB = models.IntegerField()

class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    id_BebidaCocktailDB = models.IntegerField()
    categoria = models.ForeignKey(Categoria,null=False,on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente,
                                            verbose_name=Ingrediente,
                                            default=None)
    imagen = models.ImageField(upload_to='media/')