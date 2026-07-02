# Gym Management System
# Author: Arya Rana

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="gym_management"
)
cursor = conn.cursor()
if conn.is_connected():
    print("Database connected successfully.")
else:
    print("Database connection failed.")

def accept_member():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    gender = input("Enter gender: ")
    plan = input("Enter plan (Basic/Advance): ")
    join_date = input("Enter join date (YYYY-MM-DD): ")
    query = "INSERT INTO members (first_name, last_name, gender, plan, join_date) VALUES (%s, %s, %s, %s, %s)"
    data = (first_name, last_name, gender, plan, join_date)
    cursor.execute(query, data)
    conn.commit()
    print("Member added successfully.")

def delete_member():
    member_id = input("Enter Member ID to delete: ")
    cursor.execute("DELETE FROM members WHERE id=%s", (member_id,))
    conn.commit()
    print("Member deleted.")

def modify_member():
    member_id = input("Enter Member ID to modify: ")
    new_plan = input("Enter new plan (Basic/Advance): ")
    cursor.execute("UPDATE members SET plan=%s WHERE id=%s", (new_plan, member_id))
    conn.commit()
    print("Member updated.")

def display_all():
    cursor.execute("SELECT * FROM members")
    results = cursor.fetchall()

    print("%-5s %-12s %-12s %-10s %-12s %-15s" % ("ID", "First Name", "Last Name", "Gender", "Plan", "Join Date"))
    print("-" * 70)

    for row in results:
        print("%-5s %-12s %-12s %-10s %-12s %-15s" % (row[0], row[1], row[2], row[3], row[4], str(row[5])))

def display_by_gender():
    gender = input("Enter gender to filter (Male/Female/Other): ")
    cursor.execute("SELECT * FROM members WHERE gender=%s", (gender,))
    results = cursor.fetchall()

    if results:
        print("%-5s %-12s %-12s %-10s %-12s %-15s" % ("ID", "First Name", "Last Name", "Gender", "Plan", "Join Date"))
        print("-" * 70)
        for row in results:
            print("%-5s %-12s %-12s %-10s %-12s %-15s" % (row[0], row[1], row[2], row[3], row[4], str(row[5])))
    else:
        print("No members found for this gender.")

while True:
    print("\nGym Management System")
    print("1. Accept Member")
    print("2. Delete Member")
    print("3. Modify Member")
    print("4. Display All Members")
    print("5. Display Members by Gender")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        accept_member()
    elif choice == "2":
        delete_member()
    elif choice == "3":
        modify_member()
    elif choice == "4":
        display_all()
    elif choice == "5":
        display_by_gender()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
