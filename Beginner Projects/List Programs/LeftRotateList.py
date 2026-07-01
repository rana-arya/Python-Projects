# Arya Rana
# LeftRotateList.py

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

def TEST(lst):
    first = lst.pop(0)  
    lst.append(first)  
    return lst

result = TEST(lst)
print("New list after left shift:", result)

#OUTPUT:
#Enter number of elements: 5
#Enter number: 1
#Enter number: 2
#Enter number: 3
#Enter number: 4
#Enter number: 5
#New list after left shift: [2, 3, 4, 5, 1]
