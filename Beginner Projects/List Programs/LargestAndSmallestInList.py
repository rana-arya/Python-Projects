# Arya Rana
# LargestAndSmallestInList.py

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

def TEST(lst):
    largest = max(lst)
    smallest = min(lst)
    return largest, smallest

largest, smallest = TEST(lst)
print("Largest:", largest)
print("Smallest:", smallest)

#OUTPUT:
#Enter number of elements: 5
#Enter number: 10
#Enter number: 25
#Enter number: 3
#Enter number: 19
#Enter number: 7
#Largest: 25
#Smallest: 3
