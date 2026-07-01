# Arya Rana
# AirlineManagementSystem.py
# A menu-driven Python program that uses MySQL to manage airline flight records by adding, displaying, modifying, and deleting flight information.

import mysql.connector

def TEST():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="airline"
    )
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS flights(flight_no INT PRIMARY KEY, airline VARCHAR(50), seats INT)")

    while True:
        print("1. Add Flight")
        print("2. Display Flights")
        print("3. Modify Flight")
        print("4. Delete Flight")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            flight_no = int(input("Flight Number: "))
            airline = input("Airline Name: ")
            seats = int(input("Seats: "))
            cur.execute("INSERT INTO flights VALUES(%s,%s,%s)", (flight_no, airline, seats))
            con.commit()
            print("Flight added.")
        elif choice == '2':
            cur.execute("SELECT * FROM flights")
            data = cur.fetchall()
            for row in data:
                print(row)
        elif choice == '3':
            flight_no = int(input("Enter Flight Number to modify: "))
            seats = int(input("Enter new number of seats: "))
            cur.execute("UPDATE flights SET seats=%s WHERE flight_no=%s", (seats, flight_no))
            con.commit()
            print("Flight updated.")
        elif choice == '4':
            flight_no = int(input("Enter Flight Number to delete: "))
            cur.execute("DELETE FROM flights WHERE flight_no=%s", (flight_no,))
            con.commit()
            print("Flight deleted.")
        elif choice == '5':
            break
        else:
            print("Invalid choice")

    con.close()

TEST()

#OUTPUT
# 1. Add Flight
# 2. Display Flights
# 3. Modify Flight
# 4. Delete Flight
# 5. Exit
# Enter choice: 1
# Flight Number: 201
# Airline Name: Indigo
# Seats: 180
# Flight added.
