## Exercise 1.6: Databases in Python

### Learning Goals

- Create a MySQL database for your Recipe app

### Objectives

Build a recipe_mysql.py script that will perform four basic operations through a main menu:

1. Creating recipes and adding them to the database
2. Searching for recipes on the database by ingredient
3. Modifying entries in the database
4. Deleting recipes from the database

### Part 1: Create & Connect Database

```
import mysql.connector

# Initialize a connector
conn = mysql.connector.connect(host='localhost', user='cf-python', passwd='password')

# Initialize cursor object
cursor = conn.cursor()

# Create a database as long as it doesn't already exist
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Access the database
cursor.execute("USE task_database")

# Create Recipes table
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
ingredients VARCHAR(255),
cooking_time INT,
difficulty VARCHAR(20)
)''')
```

### Part 2: Create Main Menu Loop

This method should run the user through a loop and allow them to choose from several actions. Once they select the quit option, they are taken out of the app.

```
def main_menu(conn, cursor):
.
.
.
.
    # Loop runs the main menu, continues until user selects to quit
    choice = ""
    while(choice != 'quit'):
        print("What would you like to do? Type the number of your choice!")
        print("1. Create a recipe")
        print("2. Search by ingredient")
        print("3. Update a recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exit the program.")
        choice = input("Your choice: ")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == 'quit':
            print("See you next time!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, 4 or 'quit")
    
    conn.close()
```

### Part 3: Define create_recipe()

This function should collect recipe details from the user, calculate its difficulty and insert the recipe into the Recipes table created in step 1.

```
    def create_recipe(conn, cursor):
        name = input('Enter the name for your recipe: ')
        cooking_time = int(input('Enter a cooking time (in minutes): '))
        ingredients = input('Enter the ingredients, separated by commas: ').split(', ')
        difficulty = calculate_difficulty(cooking_time, ingredients)

        ingredients_str = ", ".join(ingredients)

        sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
        val = (name, ingredients_str, cooking_time, difficulty)
        cursor.execute(sql, val)

        conn.commit()
        print("Recipe added successfully!")

    def calculate_difficulty(cooking_time, ingredients):
        num_ingredients = len(ingredients)
        if cooking_time < 10:
            if num_ingredients < 4:
                return 'Easy'
            else:
                return 'Medium'
        else:
            if num_ingredients < 4:
                return 'Intermediate'
            else:
                return 'Hard'
```

### Part 4: Define search_recipe()

This function should allow a user to select from all available ingredients and search for recipes that include that ingredient.

```
    def search_recipe(conn, cursor):
        cursor.execute("SELECT ingredients FROM Recipes")
        results = cursor.fetchall()

        all_ingredients = set()
        for row in results:
            ingredients = row[0]
            all_ingredients.update(ingredients.split(', '))

        print("\nAvailable ingredients:")
        for idx, ingredient in enumerate(sorted(all_ingredients), start=1):
            print(f"{idx}. {ingredient}")

        choice = int(input("Choose an ingredient by number to search: ")) - 1
        search_ingredient = sorted(all_ingredients)[choice]

        search_query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
        cursor.execute(search_query, ('%' + search_ingredient + '%',))
    
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No recipes found with that ingredient.")
```

### Part 5: Define update_recipe()

This function allows a user to select a recipe to update, then select which field (column) they'd like to update. The recipe item is then updated in the table.

```
    def update_recipe(conn, cursor):
        # Fetch all recipe IDs and names and present them to the user
        cursor.execute("SELECT id, name FROM Recipes")
        recipes = cursor.fetchall()
    
        print("\nAvailable Recipes:")
        for row in recipes:
            print(f"ID: {row[0]}, Name: {row[1]}")

        # Ask the user which recipe to update via ID and which detail they want to update
        recipe_id = int(input("Enter the ID of the recipe to update: "))
        column_to_update = input("Enter the item you'd like to update (name, ingredients, or cooking_time): ")

        new_value = None

        # Depending on user's selection, run code to gather new details and update the column for a given recipe
        if column_to_update == 'name':
            new_value = input("Enter the new name: ")
            update_query = "UPDATE Recipes SET name = %s WHERE id = %s"
            cursor.execute(update_query, (new_value, recipe_id))

        elif column_to_update == 'ingredients':
            # Get the new ingredients, split them into a list, then join them back into a string
            new_value = input("Enter the new ingredients (comma-separated): ").split(", ")
            new_value = ", ".join(new_value)  # Join the list into a string
            
            update_query = "UPDATE Recipes SET ingredients = %s WHERE id = %s"
            cursor.execute(update_query, (new_value, recipe_id))

        elif column_to_update == 'cooking_time':
            new_value = int(input("Enter the new cooking time (in minutes): "))
            update_query = "UPDATE Recipes SET cooking_time = %s WHERE id = %s"
            cursor.execute(update_query, (new_value, recipe_id))

        else:
            print("Invalid column.")
            return

        # If user updates ingredients or cooking_time, recalculate difficulty
        if column_to_update in ['ingredients', 'cooking_time']:
            cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))
            row = cursor.fetchone()
            difficulty = calculate_difficulty(row[0], row[1])
            update_query = "UPDATE Recipes SET difficulty = %s WHERE id = %s"
            cursor.execute(update_query, (difficulty, recipe_id))

        conn.commit()
        print("Recipe updated successfully!")
```

### Part 6: Define delete_recipe()

This function allows a user to delete a recipe from the table by selecting its ID (the primary key).

```
    def delete_recipe(conn, cursor):
        # Fetch all recipe IDs and names and present them to the user
        cursor.execute("SELECT id, name FROM Recipes")
        recipes = cursor.fetchall()
    
        print("\nAvailable Recipes:")
        for row in recipes:
            print(f"ID: {row[0]}, Name: {row[1]}")

        # Ask the user which recipe to delete via ID
        recipe_id = int(input("Enter the ID of the recipe to delete: "))

        delete_query = "DELETE FROM Recipes WHERE id = %s"
        cursor.execute(delete_query, (recipe_id,)) # trailing comma to define a tuple with a single element

        conn.commit()
        print("Recipe deleted successfully!")
```

