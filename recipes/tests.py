from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm
from django.contrib.auth.models import User
from django.urls import reverse

class RecipeModelTest(TestCase):

   def setUpTestData():
       # Set up non-modified objects used by all test methods
        Recipe.objects.create(name='Tea', ingredients='Tea Leaves, Water, Sugar', cooking_time='5', description='Delicious Tea, easy recipe')
   
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

   def test_get_absolute_url(self):
      recipe = Recipe.objects.get(id=1)
       #get_absolute_url() should take you to the detail page of book #1
       #and load the URL /books/list/1
      self.assertEqual(recipe.get_absolute_url(), '/list/1')

class RecipeFormTest(TestCase):

    def setUp(self):
        pass
    
    def test_recipe_form_valid(self):
        form_data = {'recipe_name' : 'name', 'ingredients': 'Ingredient', 'chart_type': '#1'}
        form = RecipesSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

class LoginTest(TestCase): 
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_successful_login(self):
        data = {'username': 'testuser', 'password': 'password'}
        response = self.client.post(reverse('login'), data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('recipes:list'))
        self.assertTrue(self.client.login(username='testuser', password='password'))