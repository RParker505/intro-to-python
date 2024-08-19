import pickle

recipe = {
    'name': 'Tea',
    'ingredients': ['Tea leaves', 'Sugar', 'Water'],
    'cooking_time' : 5,
    'difficulty': 'Easy'
}

my_file = open('tearecipe.bin', 'wb')
pickle.dump(recipe, my_file)
my_file.close()