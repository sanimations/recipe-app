from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, search_recipes, graph_recipes, create_recipe

app_name = 'recipes'

urlpatterns = [
   path('', home, name = 'home'),
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   path('search_recipes', search_recipes, name='search-rec'),
   path('graph_recipes', graph_recipes, name='graph-recipes'),
   path('create_recipe', create_recipe, name='create-recipe')
]