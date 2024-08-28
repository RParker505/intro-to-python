# Class variable to store all ingredients across all recipes
class Recipe:

    all_ingredients = set()  # Using a set to ensure unique ingredients

    # Initialize the Recipe object with default values.
    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = self.calculate_difficulty()
        self.update_all_ingredients()  # Add ingredients to class variable set every time a new recipe is initialized

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

# Initialize and print a few Recipe objects
tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
print(tea)

coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
print(coffee)

cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
print(cake)

banana_smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)
print(banana_smoothie)

# Wrap recipes in a list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Search for recipes containing several ingredients
recipe_search(recipes_list, "Water")
recipe_search(recipes_list, "Sugar")
recipe_search(recipes_list, "Bananas")

# Alternate way to write the searches
# for ingredient in ["Water", "Sugar", "Bananas"]:
#     recipe_search(recipes_list, ingredient)
