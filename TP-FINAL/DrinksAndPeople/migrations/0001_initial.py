# Generated by Django 3.2.9 on 2021-11-25 21:28

import DrinksAndPeople.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('id_IngredientCocktailDB', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('id_BebidaCocktailDB', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='media/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DrinksAndPeople.categoria')),
                ('ingredientes', models.ManyToManyField(default=None, to='DrinksAndPeople.Ingrediente', verbose_name=DrinksAndPeople.models.Ingrediente)),
            ],
        ),
    ]
