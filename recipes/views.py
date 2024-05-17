from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe                #to access Recipe model
from django.contrib.auth.mixins import LoginRequiredMixin   #to protect class-based view
from .forms import RecipesSearchForm, CreateRecipeForm
import pandas as pd
from django.http import HttpResponseRedirect
from .utils import get_recipename_from_id, get_chart



class RecipeListView(LoginRequiredMixin, ListView):            #class-based view
    model = Recipe                         #specify model
    main = 'recipes/recipe_list.html'    #specify template 

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    detail = 'recipes/recipe_detail.html'

def create_recipe(request):
    submitted = False
    if request.method == "POST":
        form = CreateRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_recipe?submitted=True')

    else:
        form = CreateRecipeForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'recipes/create_recipe.html', {'form': form, 'submitted': submitted})

def home(request):
   return render(request, 'recipes/recipes_home.html')

def search_recipes(request):
    form = RecipesSearchForm(request.POST or None)
    recipes_df=None   #initialize dataframe to None
    chart = None

    if request.method == "POST":
        searched = request.POST['searched']
        chart_type= '#1'
        recipes = Recipe.objects.filter(name__icontains=searched) #i makes it not case sensitive

        qs =Recipe.objects.filter(name__icontains=searched)
        print(qs)
        if qs.exists():
            recipes_df=pd.DataFrame(qs.values())
            print(recipes_df)
            recipes_df['id']=recipes_df['id'].apply(get_recipename_from_id)
            chart=get_chart(chart_type, qs)
            recipes_df=recipes_df.to_html()

        return render(request, 'recipes/search_recipes.html', 
        {'searched':searched,
        'recipes_df': recipes_df, 
        'recipes': recipes,
        'form': form,
        'chart': chart})

    else:
        return render(request, 'recipes/search_recipes.html', {})

def graph_recipes(request):
    form = RecipesSearchForm(request.POST or None)
    recipes_df = None
    chart = '#1'

    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')

        qs =Recipe.objects.filter(name=searched)
        if qs.exists():
            recipes_df=pd.DataFrame(qs.values())
            recipes_df['id']=recipes_df['id'].apply(get_recipename_from_id)
            recipes_df=recipes_df.to_html()

    context={
        'form': form,
        'recipes_df':recipes_df,
        'chart':chart
    }

    return render(request, 'recipes/graph_recipes.html', context)