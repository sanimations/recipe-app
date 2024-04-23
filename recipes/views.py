from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe                #to access Recipe model
from django.contrib.auth.mixins import LoginRequiredMixin   #to protect class-based view

class RecipeListView(LoginRequiredMixin, ListView):            #class-based view
    model = Recipe                         #specify model
    template_name = 'recipes/main.html'    #specify template 

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

def home(request):
   return render(request, 'recipes/recipes_home.html')