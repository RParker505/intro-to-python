class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"{item} has been added to the list.")
        else:
            print(f"{item} is already in the list.")
    
    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"{item} has been removed from the list.")
        else:
            print(f"{item} is not in the list.")

    def view_list(self):
        if self.shopping_list:
            print(f"{self.list_name}:")
            for item in self.shopping_list:
                print(f"- {item}")
        else:
            print(f"The shopping list '{self.list_name}' is empty.")

# Create an object called pet_store_list
pet_store_list = ShoppingList('Pet Store Shopping List')

# Add items to the list
pet_store_list.add_item('dog food')
pet_store_list.add_item('frisbee')
pet_store_list.add_item('bowl')
pet_store_list.add_item('collars')
pet_store_list.add_item('flea collars')

# Remove an item
pet_store_list.remove_item('flea collars')

# Try adding a duplicate item
pet_store_list.add_item('frisbee')

# View the full list
pet_store_list.view_list()