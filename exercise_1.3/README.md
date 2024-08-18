## Exercise 1.3: Functions and Other Operations in Python

### Learning Goals

- Implement conditional statements in Python to determine program flow
- Use loops to reduce time and effort in Python programming
- Write functions to organize Python code

### Objective

Write a python script to read any number of recipes from the user, and then add them into a list for later use, along with another list for the ingredients that you’ve come across so far. Then, you’ll display each recipe with its details, along with an extra feature—the difficulty level (calculated and displayed based on several of its own attributes).

### Step 1: Initialize empty lists
<img width="338" alt="initialize_lists" src="https://github.com/user-attachments/assets/a8cec8e6-c516-42e8-873f-c5929dec0ffd">

### Step 2: Define take_recipe funtion
Function should take inputs from the user and store them in a dictionary called **recipe**
<img width="388" alt="define_take_recipe_function" src="https://github.com/user-attachments/assets/21bb4786-16b3-4790-a1f4-f1aab788b291">

### Step 3: Determine number of recipes
Ask the user how many recipes they would like to enter. Their response will be linked to a variable n.
<img width="392" alt="ask_user_how_many_recipes" src="https://github.com/user-attachments/assets/9aeda283-e4d4-4b02-8dc8-e4c42a4bc896">

### Step 4: For loop to build ingredient and recipe lists
For loop should run `n` times to:
- Run take_recipe() and store its return output (a dictionary) in a variable called recipe.
- Iterate through the recipe's ingredients and store any new ingredients in the `ingredients_list`.
- Append the recipe to `recipes_list`.
<img width="383" alt="build_recipe_ingredients_lists" src="https://github.com/user-attachments/assets/1388f024-1726-46c3-a8b2-704c93d6bf87">

### Step 5: Determine recipe difficulty
Based on each recipe's cooking time and number of ingredients, assign it a difficulty variable.
<img width="352" alt="set_difficulty_level" src="https://github.com/user-attachments/assets/dc62e439-8565-4988-9f73-95479bae002c">

### Step 6: Display each recipe's details
<img width="347" alt="display_recipe_details" src="https://github.com/user-attachments/assets/7173bd77-85c9-4f3a-80c1-dfcb0a25fe9b">

### Step 7: Print ingredients_list
<img width="344" alt="print_all_ingredients" src="https://github.com/user-attachments/assets/45119027-6b3e-4a2b-bf90-5996b7c1feec">

#### View the code in action!
<img width="625" alt="1 3_code_test" src="https://github.com/user-attachments/assets/958b1d38-297d-4f78-abad-677397d4d5ec">

