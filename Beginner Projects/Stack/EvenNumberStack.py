# Arya Rana
# EvenNumberStack.py
# Reads a list of integers from the user, extracts the even numbers, and stores them in a stack implemented using a Python list.

def TEST():
    n = int(input("Enter number of elements: "))
    lst = []
    for i in range(n):
        lst.append(int(input("Enter element: ")))
    stack = []
    for num in lst:
        if num % 2 == 0:
            stack.append(num)
    print("List:", lst)
    print("Stack (even numbers):", stack)

TEST()

#OUTPUT
#Enter number of elements: 5
#Enter element: 1
#Enter element: 2
#Enter element: 3
#Enter element: 4
#Enter element: 5
#List: [1, 2, 3, 4, 5]
#Stack (even numbers): [2, 4]
