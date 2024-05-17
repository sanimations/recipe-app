# from django import forms


# class RecipesSearchForm(forms.Form):
#     # Define form fields for searching recipes.
#     # search_term
#     recipe_name = forms.CharField(required=False, label="Search by name") # Search By Recipe Name Optional.
#     # ingredient = forms.CharField(required=False, label="Search by ingredient") # Search By Ingredient Optional.
#     # max_cooking_time = forms.IntegerField(required=False, label="Maximum cooking time (minutes)", min_value=0) # Max Cooking Time Optional.


from django import forms
from django.forms import ModelForm
from .models import Recipe


CHART__CHOICES = (
   
    ('#1','Bar chart'),
    ('#2', 'Pie chart'), 
    ('#3', 'Line cart')
    
)

class RecipesSearchForm(forms.Form):
    recipe_name= forms.CharField(max_length=100)
    ingredients= forms.CharField(max_length=300)
    chart_type= forms.ChoiceField(choices=CHART__CHOICES)

class CreateRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = {'name', 'ingredients', 'cooking_time', 'description', 'pic'}
        labels = {
            'name': 'Recipe Name',
            'ingredients': 'List ingredients separated by commas',
        }

        widgets = { 

            'ingredients': forms.TextInput(attrs={'class':'form-control'}),
        #     'cooking_time': forms.TextInput(attrs={'class':'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'pic': forms.FileInput(attrs={'class':'form-control'}),
        }

