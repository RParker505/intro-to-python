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
