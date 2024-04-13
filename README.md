# Recipe App

## Overview
The Recipe App is a web application developed using Python and the Django framework. It aims to provide users with a platform to discover, create, and share their favorite recipes.

## Features
- **Recipes Module:** The core functionality of the application revolves around managing recipes. Users can create, edit, and delete recipes, as well as view details such as ingredients, cooking times, and difficulty.
- **Tests:** Modules are created and then the tests are created for the matching modules to continiously check for module error.

## Future Development
- **Templates:** The next phase of development will focus on creating visually appealing and responsive templates for the Recipe App. These templates will enhance the user interface, making it more engaging and accessible.
- **Views:** Alongside template development, views will be implemented to handle user requests and render appropriate responses. This includes rendering recipe details, listing recipes, and managing user interactions.


***Adding Views***

1. Open at the src folder.
2. Pick the app to create the view and navigate to the views.py file within the directory.  Define the view with a function, for the first example we created a home function:
```
from django.shortcuts import render

def home(request):
   return render(request, 'recipes/recipes_home.html')
```
Import render and use it in the home function to render the recipes_home.html

4. Create a templates folder, then create a new folder of the same name as the app, then create an html file within:
    ```
    --recipes (this is the app)
        ->templates
            ->recipes
                ->recipe_home.html
    ```

In this HTML file you create the layout for the page.

5. Create the home page URL by creating a urls.py file in the app (recipes) folder and add the following:
```
from django.urls import path
from .views import home

app_name = 'recipes'

urlpatterns = [
   path('', home),
]
```

This contains the necessary imports, including grabbing the home function from the views folder. It creates a list of urlpatterns, so far just containing the home function, which leads to the recipes_home.html file. The path name is blank, meaning it is the default link.  When running the server it will just be 'http://127.0.0.1:8000/'

*Make sure to activate the virtual environment before running the server*