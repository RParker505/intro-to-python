# Introduction To Python

## Objective
Build the command line version of a Recipe App that takes advantage of Python’s object-oriented nature. 

## Exercise 1.1

### Step 1: Install Python 3.8.7 on your system
<img width="362" alt="1 1_python_install" src="https://github.com/user-attachments/assets/6988dfcc-2244-4564-9a65-9a3e17d668f9">

### Step 2: Set up a new virtual environment
<img width="858" alt="1 1_virtual_env_creation" src="https://github.com/user-attachments/assets/e76557b7-1d3f-4826-a40c-907df18b6ee1">

### Step 3: Create a script that adds two numbers together
<img width="877" alt="1 1_add_script" src="https://github.com/user-attachments/assets/01f31b8e-5dd1-40ef-840e-8328f88d9f11">

### Step 4: Set up an IPython shell
Install IPython with `pip install ipython` from the virtual environment.
To launch the shell, run command `ipython`.

<img width="704" alt="1 1_ipython_launch" src="https://github.com/user-attachments/assets/3f6e06cb-36ba-43ba-b87c-eb8db433f67c">

### Step 5: Create requirements.txt file
Generate file with command `pip freeze > requirements.txt` from the virtual environment

_And test it with a copied environment using_ `pip install -r requirements.txt`

<img width="1255" alt="requirements_creation" src="https://github.com/user-attachments/assets/11dc418f-a1e5-449f-879d-eb402110b598">

## Exercise 1.2

### Step 1: Create recipe_1

recipe_1 should be a dictionary as it will include several key-value pairs:
- name: tea
- cooking_time: 5 (in minutes)
- ingredients: Tea leaves, Sugar, Water

<img width="617" alt="recipe_1_creation" src="https://github.com/user-attachments/assets/fbdfeb2c-fa29-43f3-97b0-7e727695b109">

### Step 2: Create all_recipes and add recipe_1 to it

all_recipes will be an outer structure to house not only recipe_1, but additional recipes as well. As it will house several dictionaries, all_recipes itself will also be a dictionary.

<img width="626" alt="all_recipes_create_add_recipe" src="https://github.com/user-attachments/assets/c0b3837e-5ac9-4390-ad17-9afa6bdfb47b">

### Step 3: Create additional recipes

The additional recipes should follow the same structure as recipe_1 and should also be added to the all_recipes dictionary.

<img width="627" alt="additional_recipes_creation" src="https://github.com/user-attachments/assets/7661aa50-15d8-4256-8cb2-fb9a3858eb54">

### Step 4: Print ingredient lists of all recipes

Use `list()` and `values()` functions to create a list of all the recipe values. Then, iterate over each recipe in the new list and print the ingredients for each recipe as a list.

<img width="623" alt="print_ingredients" src="https://github.com/user-attachments/assets/022911ec-8e30-44a1-bc80-acdd25f25bbf">



