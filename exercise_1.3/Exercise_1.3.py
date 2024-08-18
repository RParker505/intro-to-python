recipes_list = []
ingredients_list = []

# Take user input for several variables
def take_recipe():
    name = input('Enter the name for your recipe: ')
    cooking_time = int(input('Enter a cooking time (in minutes): '))
    ingredients = input('Enter the ingredients, separated by commas: ').split(', ')
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

# Ask for number of recipes to determine how many times the loop runs
n = int(input('How many recipes would you like to enter? '))

# Run for loop n times to build ingredients_list and add recipe to recipes_list
for _ in range(n):
    recipe = take_recipe()

    for i in recipe['ingredients']:
        if i not in ingredients_list:
            ingredients_list.append(i)

    recipes_list.append(recipe)

# For loop to determine recipe difficulty level
for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Hard'

# Display recipe details
for recipe in recipes_list:
    print('Recipe: ', recipe['name'])
    print('Cooking Time (min): ', recipe['cooking_time'])
    print('Ingredients: ')
    for i in recipe['ingredients']:
        print(i)
    print('Difficulty Level: ', recipe['difficulty'])

# Print ingredients_list alphabetically
def all_ingredients():
    print('Ingredients available across all recipes:')
    print('----------------------')
    ingredients_list.sort()
    for i in ingredients_list:
        print(i)

all_ingredients()
