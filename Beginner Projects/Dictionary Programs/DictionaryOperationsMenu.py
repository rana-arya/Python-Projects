# Arya Rana
# DictionaryOperationsMenu.py
# A menu-driven Python program that performs basic dictionary operations, including displaying, adding, and deleting key-value pairs.
def TEST(dic):
    while True:
        print("\nMenu:")
        print("1. Display dictionary")
        print("2. Add entry")
        print("3. Delete entry")
        print("4. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            print(dic)
        elif ch == 2:
            k = input("Enter key: ")
            v = input("Enter value: ")
            dic[k] = v
        elif ch == 3:
            k = input("Enter key to delete: ")
            if k in dic:
                del dic[k]
            else:
                print("Key not found!")
        elif ch == 4:
            break

d = {}
TEST(d)

#OUTPUT:
#Menu:
#1. Display dictionary
#2. Add entry
#3. Delete entry
#4. Exit
#Enter choice: 2
#Enter key: name
#Enter value: Arya
