# Arya Rana
# StudentTopper.py
#Reads student names and marks, stores them as tuples, and finds the student with the highest marks using Python's max() function with a lambda expression.

n = int(input("Enter number of students: "))
students = []
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append((name, marks))

def TEST(students):
    highest = max(students, key=lambda x: x[1])
    return highest

topper = TEST(students)
print("Topper is", topper[0], "with marks", topper[1])

#OUTPUT:
#Enter number of students: 3
#Enter student name: Arya
#Enter marks: 78
#Enter student name: Rahul
#Enter marks: 92
#Enter student name: Neha
#Enter marks: 85
#Topper is Rahul with marks 92
