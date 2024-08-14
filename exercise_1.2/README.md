## Exercise 1.2: Data Types in Python

### Learning Goals

- Explain variables and data types in Python
- Summarize the use of objects in Python
- Create a data structure for your Recipe app

### Objective

Create a structure that contains a set of attributes related to a specific recipe, and several of these “recipe structures” need to be stored sequentially in another outer structure.

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
