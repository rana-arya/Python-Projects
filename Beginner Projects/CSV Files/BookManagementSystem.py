# Arya Rana
# BookManagementSystem.py
# A menu-driven Python program that uses the csv module to manage book records, allowing users to add, display, search, and delete books stored in a CSV file.

import csv

def TEST():
    while True:
        print("\nMenu:")
        print("1. Add book")
        print("2. Display books")
        print("3. Search book")
        print("4. Delete book")
        print("5. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            f = open("story.csv", "a", newline="")
            w = csv.writer(f)
            w.writerow([title, author])
            f.close()
        elif ch == 2:
            f = open("story.csv", "r")
            r = csv.reader(f)
            for row in r:
                print(row)
            f.close()
        elif ch == 3:
            search = input("Enter title to search: ")
            f = open("story.csv", "r")
            r = csv.reader(f)
            found = False
            for row in r:
                if row[0] == search:
                    print("Found:", row)
                    found = True
            f.close()
            if not found:
                print("Not found!")
        elif ch == 4:
            rows = []
            f = open("story.csv", "r")
            r = csv.reader(f)
            for row in r:
                rows.append(row)
            f.close()
            search = input("Enter title to delete: ")
            f = open("story.csv", "w", newline="")
            w = csv.writer(f)
            for row in rows:
                if row[0] != search:
                    w.writerow(row)
            f.close()
            print("Book deleted if existed.")
        elif ch == 5:
            break

TEST()

#OUTPUT
#1. Add book
#2. Display books
#3. Search book
#4. Delete book
#5. Exit
