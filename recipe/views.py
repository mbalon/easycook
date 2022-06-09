from django.shortcuts import render
from django.views.generic import ListView

from .models import Recipe


class RecipeView(ListView):
    template_name = "recipes.html"
    model = Recipe
