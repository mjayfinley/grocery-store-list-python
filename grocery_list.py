lists = []


class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.items = []


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


def show_menu():
    print("Please make a selection from the following list: ")
    print(" 1. Create a Shopping List")
    print(" 2. View all Shopping Lists")
    print(" 3. Add Item to Shopping List")
    print(" q. Quit program")


def add_store():
    store_name = input("Please enter the name of your list: ")
    store = ShoppingList(store_name)
    lists.append(store)


def display_store():
    for store in lists:
        print(f'{lists.index(store) + 1} - {store.name} - {store.items}')


def add_item():
    display_store()
    store_select = int(input(
        "Please select the store you would like to add an item to: "))
    item = input("Please enter the item you would like to add: ")
    for store in lists:
        if store_select == lists.index(store) + 1:
            store.items.append(Item(item))


user_input = ''

while user_input != 'q':
    show_menu()
    user_input = input("Enter selection: ")

    if user_input == '1':
        add_store()
    elif user_input == '2':
        display_store()
    elif user_input == '3':
        add_item()
