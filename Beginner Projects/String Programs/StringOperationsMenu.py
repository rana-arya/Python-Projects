# Arya Rana
# StringOperationsMenu.py

def TEST():
    s = input("Enter a string: ")
    while True:
        print("\nMenu:")
        print("1. Length of string")
        print("2. Convert to uppercase")
        print("3. Convert to lowercase")
        print("4. Count a character")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Length:", len(s))
        elif choice == 2:
            print("Uppercase:", s.upper())
        elif choice == 3:
            print("Lowercase:", s.lower())
        elif choice == 4:
            c = input("Enter character to count: ")
            print("Count:", s.count(c))
        elif choice == 5:
            break
        else:
            print("Invalid choice!")

TEST()

#OUTPUT:
#Enter a string: Arya
#
#Menu:
#1. Length of string
#2. Convert to uppercase
#3. Convert to lowercase
#4. Count a character
#5. Exit
#Enter your choice: 1
#Length: 4
