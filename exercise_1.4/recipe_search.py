# Import pickle to work with binary files
import pickle

# Display a recipe
def display_recipe(recipe):
    print("")
    print('Recipe: ', recipe['name'])
    print('Cooking Time (min): ', recipe['cooking_time'])
    print('Ingredients: ')
    for i in recipe['ingredients']:
        print("- ", i)
    print('Difficulty Level: ', recipe['difficulty'])
    print("")

# Search for an ingredient
def search_ingredient(data):
    # Print all available ingredients with indexes starting at 1
    print('All Available Ingredients:')
    for index, ingredient in enumerate(data['all_ingredients'], 1):
        print(f"{index}. {ingredient}")

    # Ask user to pick a number and store the indexed ingredient into a new variable
    pick = int(input('Enter the number of an ingredient to search: ')) -1

    try:
        ingredient_searched = data['all_ingredients'][pick]
    except:
        print("Oops, that input is invalid! Please choose a valid number from the list.")
        return
    else:
        print(f"\nRecipes containing '{ingredient_searched}':")
        found = False
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found = True
        if not found:
            print(f"No recipes found containing the ingredient '{ingredient_searched}'.")

# Ask for filename to open binary file and load data
filename = input('Enter the name of the file where your recipes are stored: ')

try:
    file = open(filename, 'rb')
    data = pickle.load(file)
except FileNotFoundError:
    print("Oops, that file was not found! Please make sure the file name is correct.")
else:
    search_ingredient(data)