# Arya Rana
# RailwayManagementSystem.py
# A menu-driven Python application that connects to a MySQL database to manage train records, including adding, displaying, and searching trains.

import mysql.connector

def TEST():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="railway"
    )
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS trains(train_no INT PRIMARY KEY, name VARCHAR(50), source VARCHAR(50), destination VARCHAR(50))")

    while True:
        print("1. Add Train")
        print("2. Display Trains")
        print("3. Search Train")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            train_no = int(input("Train Number: "))
            name = input("Train Name: ")
            source = input("Source: ")
            dest = input("Destination: ")
            cur.execute("INSERT INTO trains VALUES(%s,%s,%s,%s)", (train_no, name, source, dest))
            con.commit()
            print("Train added.")
        elif choice == '2':
            cur.execute("SELECT * FROM trains")
            data = cur.fetchall()
            for row in data:
                print(row)
        elif choice == '3':
            train_no = int(input("Enter Train Number to search: "))
            cur.execute("SELECT * FROM trains WHERE train_no=%s", (train_no,))
            data = cur.fetchall()
            for row in data:
                print(row)
        elif choice == '4':
            break
        else:
            print("Invalid choice")

    con.close()

TEST()

#OUTPUT
# 1. Add Train
# 2. Display Trains
# 3. Search Train
# 4. Exit
# Enter choice: 1
# Train Number: 101
# Train Name: Shatabdi
# Source: Delhi
# Destination: Agra
# Train added.
