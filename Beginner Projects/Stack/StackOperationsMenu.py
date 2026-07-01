# Arya Rana
# StackOperationsMenu.py
# A menu-driven Python program that implements a stack using a list, supporting push, pop, and display operations.

def TEST():
    stack = []
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            item = input("Enter element to push: ")
            stack.append(item)
        elif ch == 2:
            if len(stack) == 0:
                print("Stack is empty!")
            else:
                print("Popped:", stack.pop())
        elif ch == 3:
            print("Stack:", stack)
        elif ch == 4:
            break

TEST()

#OUTPUT
#1. Push
#2. Pop
#3. Display
#4. Exit
