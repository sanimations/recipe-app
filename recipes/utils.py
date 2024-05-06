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

    #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
    #AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')

    #specify figure size
    fig=plt.figure(figsize=(6,3))

    #select chart_type based on user input from the form
    if chart_type == '#1':
        #plot bar chart between date on x-axis and quantity on y-axis
        plt.bar(data['name'], data['ingredients'])

    else:
        return None