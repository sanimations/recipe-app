# from django import forms


# class RecipesSearchForm(forms.Form):
#     # Define form fields for searching recipes.
#     # search_term
#     recipe_name = forms.CharField(required=False, label="Search by name") # Search By Recipe Name Optional.
#     # ingredient = forms.CharField(required=False, label="Search by ingredient") # Search By Ingredient Optional.
#     # max_cooking_time = forms.IntegerField(required=False, label="Maximum cooking time (minutes)", min_value=0) # Max Cooking Time Optional.


from django import forms


CHART__CHOICES = (
   
    ('#1','Bar chart'),
    ('#2', 'Pie chart'), 
    ('#3', 'Line cart')
    
)

class RecipesSearchForm(forms.Form):
    recipe_name= forms.CharField(max_length=100)
    ingredients= forms.CharField(max_length=300)
    chart_type= forms.ChoiceField(choices=CHART__CHOICES)
