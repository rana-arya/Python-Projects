# Arya Rana
# BankCustomerManagement.py
# A menu-driven Python program that uses MySQL to manage bank customer records by adding and displaying customer information.

import mysql.connector

def TEST():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank"
    )
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customers(acc_no INT PRIMARY KEY, name VARCHAR(50), balance FLOAT)")

    while True:
        print("1. Add Customer")
        print("2. Display Customers")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            acc_no = int(input("Account Number: "))
            name = input("Name: ")
            balance = float(input("Balance: "))
            cur.execute("INSERT INTO customers VALUES(%s,%s,%s)", (acc_no, name, balance))
            con.commit()
            print("Customer added.")
        elif choice == '2':
            cur.execute("SELECT * FROM customers")
            data = cur.fetchall()
            for row in data:
                print(row)
        elif choice == '3':
            break
        else:
            print("Invalid choice")

    con.close()

TEST()

#OUTPUT
# 1. Add Customer
# 2. Display Customers
# 3. Exit
# Enter choice: 1
# Account Number: 101
# Name: Arya
# Balance: 5000
# Customer added.
# Enter choice: 2
# (101, 'Arya', 5000.0)
