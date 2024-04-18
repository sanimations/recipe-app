from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=75) 
    ingredients = models.TextField()
    cooking_time = models.FloatField(help_text='in minutes')
    description = models.TextField(default="")  #Description for user to write about the dish and the steps to make it
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
	    return reverse ('recipes:detail', kwargs={'pk': self.pk})

    def ingredients_list(self):
        return self.ingredients.split(",")

    def calc_difficulty(self):
        num_ingredients = len(self.ingredients_list())
        if self.cooking_time < 10 and num_ingredients < 4:
            return 'Easy'
        elif self.cooking_time < 10 and num_ingredients >= 4:
            return 'Medium'
        elif self.cooking_time >= 10 and num_ingredients < 4:
            return 'Intermediate'
        elif self.cooking_time >= 10 and num_ingredients >= 4:
            return 'Hard'