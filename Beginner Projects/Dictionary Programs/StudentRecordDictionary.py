# Arya Rana
# StudentRecordDictionary.py
# Accepts student details (roll number, name, and marks), stores them in a dictionary, and displays all student records.

n = int(input("Enter number of students: "))
dic = {}
for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    dic[roll] = (name, marks)

def TEST(dic):
    for roll, data in dic.items():
        print("Roll:", roll, "Name:", data[0], "Marks:", data[1])

TEST(dic)

#OUTPUT:
#Enter number of students: 2
#Enter roll number: 1
#Enter name: Arya
#Enter marks: 80
#Enter roll number: 2
#Enter name: Neha
#Enter marks: 90
#Roll: 1 Name: Arya Marks: 80
#Roll: 2 Name: Neha Marks: 90
