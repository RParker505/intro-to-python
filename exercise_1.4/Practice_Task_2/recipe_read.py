import pickle

with open('tearecipe.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print("Recipe details - ")
print("Name:  " + recipe['name'])
print("Ingredients:  " + ", ".join(recipe["ingredients"]))
print("Cooking Time: " + str(recipe['cooking_time']) + " minutes")
print("Difficulty:  " + recipe['difficulty'])