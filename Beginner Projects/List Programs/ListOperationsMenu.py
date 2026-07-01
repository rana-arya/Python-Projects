# Arya Rana
# ListOperationsMenu.py
# Reads a list of numbers from the user and allows operations such as displaying, sorting, and reversing the list through a menu-driven program.

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input("Enter element: ")))

def TEST(lst):
    while True:
        print("\nMenu:")
        print("1. Display list")
        print("2. Sort list")
        print("3. Reverse list")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("List:", lst)
        elif choice == 2:
            lst.sort()
            print("Sorted list:", lst)
        elif choice == 3:
            lst.reverse()
            print("Reversed list:", lst)
        elif choice == 4:
            break
        else:
            print("Invalid choice!")

TEST(lst)

#OUTPUT:
#Enter number of elements: 4
#Enter element: 12
#Enter element: 4
#Enter element: 9
#Enter element: 20
#
#Menu:
#1. Display list
#2. Sort list
#3. Reverse list
#4. Exit
#Enter choice: 1
#List: [12, 4, 9, 20]
