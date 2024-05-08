from io import BytesIO 
import base64
import matplotlib.pyplot as plt
from recipes.models import Recipe
from collections import Counter
from django.shortcuts import get_object_or_404

def get_recipename_from_id(val):
    recipename=Recipe.objects.get(id=val)
    return recipename

def get_graph():
    #create a BytesIO buffer for the image
    buffer = BytesIO()         

    #create a plot with a bytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format='png')

    #set cursor to the beginning of the stream
    buffer.seek(0)

    #retrieve the content of the file
    image_png=buffer.getvalue()

    #encode the bytes-like object
    graph=base64.b64encode(image_png)

    #decode to get the string as output
    graph=graph.decode('utf-8')

    #free up the memory of buffer
    buffer.close()

    #return the image/graph
    return graph

#chart_type: user input o type of chart,
#data: pandas dataframe

def get_chart(chart_type, data):

    fig, ax = plt.subplots(figsize=(13,6))

    ingredients = []
    ingredients_count = []

    for recipe in data:
        ingredients_list = getattr(recipe, 'ingredients').split(',')
        for ingredient in ingredients_list:
            ingredient = ingredient.strip()
            if ingredient in ingredients:
                dup_index = ingredients.index(ingredient)
                ingredients_count[dup_index] += 1
            else:
                ingredients.append(ingredient)
                ingredients_count.append(1)



    ax.bar(ingredients, ingredients_count, width=0.5)

    ax.set_ylabel('Ingredient Supply')
    ax.set_title('Ingredients Count In Each Recipe')

    buf = BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()

    return image_base64
