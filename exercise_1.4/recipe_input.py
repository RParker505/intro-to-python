# Import pickle to work with binary files
import pickle

# Take user recipe details and return a recipe dictionary
def take_recipe():
    name = input('Enter the name for your recipe: ')
    cooking_time = int(input('Enter a cooking time (in minutes): '))
    ingredients = input('Enter the ingredients, separated by commas: ').split(', ')
    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients, 'difficulty': difficulty}
    return recipe

# Determine recipe difficulty level
def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        return 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
        return 'Intermediate'
    elif cooking_time >= 10 and len(ingredients) >= 4:
        return 'Hard'

# Ask for filename to open binary file
filename = input('Enter the name of the file where your recipes are stored: ')

try:
    # Attempt to open the binary file in read mode and load it using pickle
    file = open(filename, 'rb')
    data = pickle.load(file)
    print("File loaded successfully!")
except FileNotFoundError:
    print("That file was not found - A new file will be created.")
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print("Oops, there was an issue - A new file will be created.")
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    file.close()
finally:
    # Extract values from the dictionary into separate lists
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

# Ask for number of recipes to determine how many times the loop runs
n = int(input('How many recipes would you like to enter? '))

# Run for loop n times to build ingredients_list and add recipe to recipes_list
for _ in range(n):
    recipe = take_recipe()

    for i in recipe['ingredients']:
        if i not in all_ingredients:
            all_ingredients.append(i)

    recipes_list.append(recipe)

    print("Recipe added successfully!")

# Creates the data dictionary with recipe lists
data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

# Open user's binary file in write mode and add data dictionary using pickle
with open(filename, 'wb') as file:
    pickle.dump(data, file)
print("Your recipe file has been updated!")