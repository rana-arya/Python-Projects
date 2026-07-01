# Arya Rana
# MySQLCRUDOperations.py
# A Python program that connects to a MySQL database and performs CRUD (Create, Read, Update, Delete) operations on a student table.

import mysql.connector

def TEST():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
    )
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS students(id INT PRIMARY KEY, name VARCHAR(50), marks INT)")

   
    cur.execute("INSERT INTO students VALUES(1, 'Arya', 95)")
    cur.execute("INSERT INTO students VALUES(2, 'Rana', 88)")
    con.commit()

    
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    for row in data:
        print(row)

    
    cur.execute("UPDATE students SET marks=100 WHERE id=1")
    con.commit()

    
    cur.execute("DELETE FROM students WHERE id=2")
    con.commit()

    con.close()

TEST()

#OUTPUT
# (1, 'Arya', 95)
# (2, 'Rana', 88)

