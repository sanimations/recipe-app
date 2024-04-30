from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe                #to access Recipe model
from django.contrib.auth.mixins import LoginRequiredMixin   #to protect class-based view
from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart


class RecipeListView(LoginRequiredMixin, ListView):            #class-based view
    model = Recipe                         #specify model
    main = 'recipes/recipe_list.html'    #specify template 


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    detail = 'recipes/recipe_detail.html'

def home(request):
   return render(request, 'recipes/recipes_home.html')

def records(request):
    #create an instance of RecipesSearchForm that you defined in recipes/forms.py
    form = RecipesSearchForm(request.POST or None)
    recipes_df = None
    chart = None

     #check if the button is clicked
    if request.method =='POST':
        recipe_name = request.POST.get('recipe_name')
        ingredients = request.POST.get('ingredients')
        chart_type = request.POST.get('chart_type')

        qs =Recipe.objects.filter(name=recipe_name, ingredients=ingredients)
        if qs.exists():
            recipes_df=pd.DataFrame(qs.values())
            recipes_df['recipe_id']=recipes_df['recipe_id'].apply(get_recipename_from_id)
            chart=get_chart(chart_type, recipes_df, labels=recipes_df['date_created'].values)
            recipes_df=recipes_df.to_html()

        # print(recipe_name, ingredients,chart_type)

        # print ('Exploring querysets:')
        # print ('Case 1: Output of Sale.objects.all()')
        # qs=Recipe.objects.all()
        # print (qs)

        # print ('Case 2: Output of Sale.objects.filter(book_name=book_title)')
        # qs =Recipe.objects.filter(book__name=book_title)
        # print (qs)

        # print ('Case 3: Output of qs.values')
        # print (qs.values())

        # print ('Case 4: Output of qs.values_list()')
        # print (qs.values_list())

        # print ('Case 5: Output of Sale.objects.get(id=1)')
        # obj = Recipe.objects.get(id=1)
        # print (obj)

        context={
          'form': form,
          'recipes_df': recipes_df,
          'chart': chart
        }

    return render(request, 'recipes/recipe_list.html', context)
