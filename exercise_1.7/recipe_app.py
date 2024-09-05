# Import packages and methods
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

# Create engine object to connect to database
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# Store declarative base
Base = declarative_base()

# Create session object to make changes to database
Session = sessionmaker(bind=engine)
session = Session()

# Define Recipe model
class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Quick info on the recipe
    def __repr__(self):
        return f"<Recipe ID: {self.id} - Name: {self.name} - Difficulty: {self.difficulty}>"

    # Full recipe printout
    def __str__(self):
        return (
            f"{'-'*5}\n"
            f"Recipe: {self.name}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Ingredients: {self.ingredients}\n"
            f"Difficulty: {self.difficulty}\n"
            f"{'-'*5}\n"
            "Enjoy!"
        )

    # Calculate recipe difficulty
    def calculate_difficulty(self):
        ing_list = self.ingredients.split(', ')
        num_ingredients = len(ing_list)
        if self.cooking_time < 10:
            if num_ingredients < 4:
                self.difficulty ='Easy'
            else:
                self.difficulty = 'Medium'
        else:
            if num_ingredients < 4:
                self.difficulty = 'Intermediate'
            else:
                self.difficulty = 'Hard'

    # Return ingredients as a list
    def return_ingredients_as_list():
        if not self.ingredients:  # Check if ingredients string is empty
            return []
        else:
            return self.ingredients.split(', ')

# Create the table on the database
Base.metadata.create_all(engine)

# Define main menu functions

def create_recipe():
    # Collect and validate recipe name
    while True:
        name = input('Enter the name for your recipe: ')
        if len(name) > 50:
            print("Error: Name cannot be longer than 50 characters. Try again.")
        elif not name.isalpha():
            print("Error: Name must contain only letters. Try again.")
        else:
            break

    # Collect and validate cooking time
    while True:
        cooking_time = input('Enter a cooking time (in minutes): ')
        if not cooking_time.isnumeric():
            print("Error: Cooking time must be a number. Try again.")
        else:
            cooking_time = int(cooking_time)
            break

    # Collect ingredients        
    ingredients = []
    n = int(input('How many ingredients does the recipe have? '))

    for i in range(n):
        ingredient = input(f'Enter ingredient {i+1}: ')
        ingredients.append(ingredient)

    # Convert ingredients list into a string
    ing_string = ', '.join(ingredients)

    # Create new Recipe object
    recipe_entry = Recipe(
        name = name,
        cooking_time = cooking_time,
        ingredients = ing_string
    )

    # Calculate and set difficulty
    recipe_entry.calculate_difficulty()

    # Add recipe to session and commit to database
    session.add(recipe_entry)
    session.commit()

    print("Recipe added successfully!")

def view_all_recipes():
    # Retrieve all recipes in database as a list
    recipes_list = session.query(Recipe).all()

    # Check if list is empty
    if not recipes_list:
        print("No recipes found in the database.")
        return None

    # Call __str__ method to print all recipes
    for recipe in recipes_list:
        print(recipe)

def search_by_ingredients():
    # Check for table entries
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("No recipes found in the database.")
        return None
    
    # Retrieve ingredients column only
    results = session.query(Recipe.ingredients).all()

    # Initialize empty ingredients list
    all_ingredients = []

    # Split ingredients into list, append to all_ingredients if not already there
    for result in results:
        ingredients_list = result[0].split(', ')
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    # Display available ingredients and ask which to search
    print("\nAvailable ingredients:")
    for idx, ingredient in enumerate(all_ingredients, start=1):
        print(f"{idx}. {ingredient}")
    selected_ingredients = input("Enter the numbers of the ingredients you'd like to search for (separated by spaces): ")

    # Check if user input is valid
    try:
        selected_indices = [int(i) for i in selected_ingredients.split()]
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by spaces.")
        return None

    if any(i < 1 or i > len(all_ingredients) for i in selected_indices):
        print("Error: Invalid selection. Please enter numbers from the displayed options.")
        return None

    # Make a list of the selected ingredients to search for
    search_ingredients = [all_ingredients[i-1] for i in selected_indices]

    # Initialize empty conditions list
    conditions = []

    # Loop through search_ingredients and create like() conditions
    for ing in search_ingredients:
        like_term = f'%{ing}%'
        conditions.append(Recipe.ingredients.like(like_term))

    # Retrieve recipes from the database using filter() with conditions
    # Use 'and_' to combine the conditions so that all ingredients must be present
    from sqlalchemy import and_
    matching_recipes = session.query(Recipe).filter(and_(*conditions)).all()

    if not matching_recipes:
        print("No recipes found including all your selected ingredients.")
    else:
        for recipe in matching_recipes:
            print(recipe)

def edit_recipe():
    # Check for table entries
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("No recipes found in the database.")
        return None

    # Retrieve id and name of each recipe
    results = session.query(Recipe.id, Recipe.name).all()

    # Display recipes to user
    print("\nAvailable recipes:")
    for recipe in results:
        print(f"ID: {recipe.id} - Name: {recipe.name}")

    # Ask user to select a recipe by id to update
    selected_id = input("Enter the ID of the recipe you'd like to update: ")
    if not selected_id.isnumeric() or int(selected_id) not in [r.id for r in results]:
        print("Error: You must select an available recipe by its ID. Try again")
        return None

    # Retrieve recipe that corresponds with the selected ID
    recipe_to_edit = session.query(Recipe).filter_by(id=int(selected_id)).one()

    # Print the selected recipe details
    print("Recipe details:")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Ingredients: {recipe_to_edit.ingredients}")
    print(f"3. Cooking Time: {recipe_to_edit.cooking_time} minutes")

    # Ask which field they want to update
    choice = input("Enter the number of the field you'd like to update (1, 2 or 3): ")

    if choice not in ['1', '2', '3']:
        print("Invalid choice.")
        return None

    # Edit the attribute based on user choice
    if choice == '1':
        new_name = input("Enter the new name: ")
        if len(new_name) > 50 or not new_name.isalpha():
            print("Error: Name must be letters only and no longer than 50 characters.")
            return None
        recipe_to_edit.name = new_name

    elif choice == '2':
        new_ingredients = []
        n = int(input('How many ingredients does the recipe have? '))

        for i in range(n):
            ingredient = input(f'Enter ingredient {i+1}: ')
            new_ingredients.append(ingredient)
        
        recipe_to_edit.ingredients = ', '.join(new_ingredients)

    if choice == '3':
        new_time = input("Enter the new cooking time (in minutes): ")
        if not new_time.isnumeric():
            print("Error: Cooking time must be a number.")
            return None
        recipe_to_edit.cooking_time = int(new_time)

    # Recalculate difficulty
    recipe_to_edit.calculate_difficulty()

    session.commit()

    print("Recipe updated successfully!")

def delete_recipe():
    # Check for table entries
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("No recipes found in the database.")
        return None

    # Retrieve id and name of each recipe
    results = session.query(Recipe.id, Recipe.name).all()

    # Display recipes to user
    print("\nAvailable recipes:")
    for recipe in results:
        print(f"ID: {recipe.id} - Name: {recipe.name}")

    # Ask user to select a recipe by id to update
    selected_id = input("Enter the ID of the recipe you'd like to delete: ")
    if not selected_id.isnumeric() or int(selected_id) not in [r.id for r in results]:
        print("Error: You must select an available recipe by its ID. Try again")
        return None

    # Convert input to integer
    selected_id = int(selected_id)

    # Retrieve recipe that corresponds with the selected ID
    recipe_to_delete = session.query(Recipe).filter_by(id=selected_id).one()

    # Confirm the deletion
    choice = input(f"Are you sure you want to delete the recipe '{recipe_to_delete.name}'? Enter 'yes' or 'no': ").lower()

    # Actions based on user confirmation
    if choice == 'no':
        print("Recipe will not be deleted.")
        return None

    elif choice == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe has been deleted!")

    else:
        print("Invalid choice. You must enter either 'yes' or 'no' exactly.")
        return None
        
# Main Menu
# Loop runs the main menu, continues until user selects to quit
user_choice = ""
while user_choice != 'quit':
    print("\nWelcome! What would you like to do? Type the number of your choice!")
    print("1. Create a recipe")
    print("2. View all recipes")
    print("3. Search by ingredient")
    print("4. Update a recipe")
    print("5. Delete a recipe")
    print("Type 'quit' to exit the program.")

    user_choice = input("Your choice: ")

    if user_choice == '1':
        create_recipe()
    elif user_choice == '2':
        view_all_recipes()
    elif user_choice == '3':
        search_by_ingredients()
    elif user_choice == '4':
        edit_recipe()
    elif user_choice == '5':
        delete_recipe()
    elif user_choice == 'quit':
        print("See you next time!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, 4, 5 or 'quit'.")

# Close session and engine
session.close()
engine.dispose()