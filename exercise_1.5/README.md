## Exercise 1.5: Object-Oriented Programming in Python

### Learning Goals

- Apply object-oriented programming concepts to your Recipe app

### Objectives

1. Build a Recipe class with relevant data and procedural attributes.
2. Create and store recipes using class methods (same as procedural attributes).
3. Use these class methods to search for recipes according to specific ingredients.

### Part 1: Define Recipe class

Define a class Recipe, with the following data attributes:
- name: the name of a recipe
- ingredients: a list containing the ingredients for a recipe
- cooking_time: the time taken in minutes to carry out a recipe
- difficulty: an auto-generated attribute that says whether the recipe is Easy, Medium, Intermediate, or Hard based on a calc_difficulty() method to be defined later

```
    # Initialize the Recipe object with default values.
    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()
        self.update_all_ingredients()  # Add ingredients to class variable set every time a new recipe is initialized
```

### Part 2: Define procedural attributes (methods) for the class
- An initialization method that takes in the name and other data attributes for the recipe
- Getter and setter methods for name and cooking_time
- A method called `add_ingredients` that takes in variable-length arguments for the recipe’s ingredients and adds them to ingredients. Once all the ingredients are added, this function calls `update_all_ingredients()`
- A getter method for ingredients that returns the list itself
- A method called `calculate_difficulty()` that calculates and updates the difficulty of the recipe
- A getter method for difficulty which also calls `calculate_difficulty()` if difficulty hasn’t been calculated
- A search method called `search_ingredient()` that takes an ingredient as an argument, searches for it in the recipe, and returns True or False appropriately
- A method called `update_all_ingredients()` that goes through the current object’s ingredients and adds them to a class variable called `all_ingredients` if they’re not already present. This class variable keeps track of all the ingredients that exist across all recipes.
- A string representation that prints the entire recipe over a well formatted string.

```
    # Setter method for name
    def set_name(self, name):
        self.name = name
        
    # Getter method for name
    def get_name(self):
        return self.name

    # Setter method for cooking_time
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        
    # Getter method for cooking_time
    def get_cooking_time(self):
        return self.cooking_time

    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10:
            if num_ingredients < 4:
                return 'Easy'
            else:
                return 'Medium'
        else:
            if num_ingredients < 4:
                return 'Intermediate'
            else:
                return 'Hard'
    
    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients # Boolean output

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            Recipe.all_ingredients.add(ingredient) # use add() method for the all_ingredients set

    def __str__(self):
        output = "\nRecipe: " + str(self.name) + \
            "\nCooking Time: " + str(self.cooking_time) + " minutes" + \
            "\nDifficulty: " + str(self.get_difficulty()) + \
            "\nIngredients:\n"
        for ingredient in self.ingredients:
                output += "- " + ingredient + "\n"
        return output
```

### Part 3: Define method to search an ingredient

`recipe_search()` takes two parameters:
- data: takes in a list of Recipe objects to search from
- search_term: the ingredient to be searched for

A for loop traverses through data, within the object that is in focus, it calls the `search_ingredient()` method to see if the ingredient is present or not. If the condition is satisfied, print the recipe.

```
# Standalone method outside Recipe class
# Parameters:
# data: list of Recipe objects to search from
# search_term: the ingredient to be searched for
def recipe_search(data, search_term):
    print(f"Recipes that contain '{search_term}':\n")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
            print("-" * 30) # Spacer for readability
```

### Part 4: Inititalize Recipe Objects

Create several objects with varying cook times and ingredient lists. Print them.

```
# Initialize and print a few Recipe objects
tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
print(tea)

coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
print(coffee)

cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
print(cake)

banana_smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)
print(banana_smoothie)
```

### Part 5: Search for Ingredients

Add the recipe objects to a list and use the `recipe_search()` method to search for recipes that contain each of several ingredients.

```
# Wrap recipes in a list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Search for recipes containing several ingredients
recipe_search(recipes_list, "Water")
recipe_search(recipes_list, "Sugar")
recipe_search(recipes_list, "Bananas")
```
