## Exercise 1.4: File Handling in Python

### Learning Goals

- Use files to store and retrieve data in Python

### Objective

Write a **recipe_input.py** script that takes recipes from the user, compiles them and their ingredients into a list, and stores all this in a binary file for later use. The script can be run again later to add more recipes. Then, write a **recipe_search.py** script to accesses the binary file and lists all the ingredients that are available. The user enters an ingredient, and the script displays every recipe containing that specific ingredient.

### Part 1: recipe_input.py Script

#### Step 1: Import pickle
Include `import pickle` at top of the script file so that you can work with binary files

#### Step 2: Define take_recipe()
This function should take user input for a recipe and store it in a dictionary called **recipe**.

<img width="655" alt="image" src="https://github.com/user-attachments/assets/5c535f9b-8c8d-4c4f-8b54-54a1ea27ce07">

#### Step 3: Define calc_difficulty()
This function, which is called in take_recipe(), should determine the difficulty level of a recipe based on its cooking_time and ingredients

<img width="329" alt="image" src="https://github.com/user-attachments/assets/bcf84169-9b09-476d-abbf-21a3d40d39ed">

#### Step 4: Write the main code
Have the user enter a filename, which would attempt to open a binary file in read mode.

A try-except-else-finally block should be used to deal with FileNotFoundError and other potential errors. The try block attempts to open the given file and load its contents through the pickle module into a variable called data. The incoming data is expected to be a dictionary containing two key-value pairs:
- recipes_list (a list of all recipes)
- all_ingredients (a list of all ingredients across all recipes)

The except blocks will create a new dictionary called data, which contains the recipes list under the key recipes_list and another list containing all the ingredients under all_ingredients.

If no errors are encountered and the except blocks are skipped, the else block should close the file stream.

The finally block extracts the values from the data dictionary into two separate lists: recipes_list and all_ingredients.

<img width="466" alt="image" src="https://github.com/user-attachments/assets/43096870-5068-45c1-8ba6-f4c2ebc28f3d">

#### Step 5: Determine number of recipes to add
Ask the user how many recipes they’d like to enter, and define a for loop that calls the take_recipe() function. You can append the output of this function into recipes_list. Next, define an inner loop that scans through the recipe’s ingredients and adds them to all_ingredients if they’re not already there.

<img width="472" alt="image" src="https://github.com/user-attachments/assets/167c57c1-7f52-4f25-b58f-0d8d1626ed27">

#### Step 6: Create data dictionary
Gather the updated recipes_list and all_ingredients into the dictionary called data.

<img width="439" alt="image" src="https://github.com/user-attachments/assets/27c57fc6-00aa-47ae-9602-44792b95db5d">

#### Step 7: Open binary file and add dictionary
Open a binary file with the user-defined filename and write data to it using the pickle module.

<img width="452" alt="image" src="https://github.com/user-attachments/assets/d72e6678-a67b-4533-a319-acfe30220dde">

See the code in action!

<img width="625" alt="recipe_input_code_test" src="https://github.com/user-attachments/assets/6e6cd4cc-379b-4767-8369-6385cc78a6cc">
