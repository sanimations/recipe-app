from django.urls import path
from .views import home
from .views import RecipeListView, RecipeDetailView
from .views import search_recipes
from .views import graph_recipes

app_name = 'recipes'

urlpatterns = [
   path('', home, name = 'home'),
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   path('search_recipes', search_recipes, name='search-rec'),
   path('graph_recipes', graph_recipes, name='graph-recipes'),
]