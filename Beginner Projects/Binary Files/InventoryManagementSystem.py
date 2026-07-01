# Arya Rana
# InventoryManagementSystem.py
# A menu-driven Python program that uses the pickle module to manage inventory records in a binary file, with options to add, display, search, and delete items.

import pickle

def TEST():
    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Display items")
        print("3. Search item")
        print("4. Delete item")
        print("5. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            item = input("Enter item: ")
            price = int(input("Enter price: "))
            data = [item, price]
            f = open("story.dat", "ab")
            pickle.dump(data, f)
            f.close()
        elif ch == 2:
            try:
                f = open("story.dat", "rb")
                while True:
                    data = pickle.load(f)
                    print(data)
            except EOFError:
                f.close()
        elif ch == 3:
            search = input("Enter item to search: ")
            found = False
            f = open("story.dat", "rb")
            try:
                while True:
                    data = pickle.load(f)
                    if data[0] == search:
                        print("Found:", data)
                        found = True
            except EOFError:
                f.close()
            if not found:
                print("Not found!")
        elif ch == 4:
            items = []
            f = open("story.dat", "rb")
            try:
                while True:
                    items.append(pickle.load(f))
            except EOFError:
                f.close()
            search = input("Enter item to delete: ")
            f = open("story.dat", "wb")
            for d in items:
                if d[0] != search:
                    pickle.dump(d, f)
            f.close()
            print("Item deleted if existed.")
        elif ch == 5:
            break

TEST()

#OUTPUT
#1. Add item
#2. Display items
#3. Search item
#4. Delete item
#5. Exit
