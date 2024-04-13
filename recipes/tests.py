from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    def setUpTestData():
       # Set up non-modified objects used by all test methods
        Recipe.objects.create(name='Tea', ingredients='Tea Leaves, Water, Sugar', cooking_time='5')
   
    def test_recipe_name(self):
       # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

       # Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('name').verbose_name

       # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_ingredients_max_length(self):
           # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

           # Get the metadata for the 'ingredients' field and use it to query its max_length
        max_length = recipe._meta.get_field('ingredients').max_length

           # Compare the value to the expected result i.e. 400
        self.assertEqual(max_length, 400)