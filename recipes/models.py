from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=400)
    cooking_time = models.FloatField(help_text='in minutes')


    def __str__(self):
        return str(self.name)