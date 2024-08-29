class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item: str):
        if item not in self.items:
            self.items.append(item)
            print(f"'{item}' has been added to the shopping list.")
        else:
            print(f"'{item}' is already in the shopping list.")

    def remove_item(self, item: str):
        if item in self.items:
            self.items.remove(item)
            print(f"'{item}' has been removed from the shopping list.")
        else:
            print(f"'{item}' is not in the shopping list.")

    def search_item(self, item: str) -> bool:
        return item in self.items

    def display_list(self):
        if self.items:
            print("Current shopping list:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("The list is currently empty.")

    def reverse_list(self):
        self.items.reverse()
        print("The shopping list has been reversed.")

if __name__ == "__main__":
    my_shopping_list = ShoppingList()
    my_shopping_list.add_item("Bread")
    my_shopping_list.add_item("Milk")
    my_shopping_list.add_item("Eggs")
    my_shopping_list.add_item("Bread")

    my_shopping_list.display_list()

    item_to_search = input("Enter item to search: ")
    if my_shopping_list.search_item(item_to_search):
        print(f"'{item_to_search}' is on the shopping list.")
    else:
        print(f"'{item_to_search}' is not on the shopping list.")
    
    item_to_remove = input("Enter item to remove: ")
    my_shopping_list.remove_item(item_to_remove)

    my_shopping_list.display_list()

    # Adding functionality to reverse the list
    reverse_choice = input("Do you want to reverse the list? (yes/no): ").strip().lower()
    if reverse_choice == "yes":
        my_shopping_list.reverse_list()
        my_shopping_list.display_list()
