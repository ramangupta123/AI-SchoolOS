# AI-SchoolOS Notes

# Day 1 - MySQL + Python CRUD

---

# What is CRUD?

CRUD is the four basic database operations.

C → Create → INSERT

R → Read → SELECT

U → Update → UPDATE

D → Delete → DELETE

Almost every backend application uses CRUD.

---

# database.py

Purpose:
Connect Python with MySQL.

Contains:

- connection
- cursor

This file should NOT contain business logic.

---

# Connection

connection = mysql.connector.connect(...)

Purpose:

Connect Python to the MySQL Server.

Think:

Python 📞 MySQL

---

# Cursor

cursor = connection.cursor()

Purpose:

Executes SQL queries.

Think:

Cursor = Messenger

Python
↓

Cursor
↓

MySQL

---

# execute()

cursor.execute(query)

Purpose:

Sends the SQL query to MySQL.

Without execute(), SQL is just a string.

---

# commit()

connection.commit()

Purpose:

Permanently save changes.

Required after:

INSERT

UPDATE

DELETE

Not required after SELECT.

Think:

Google Docs → Save

---

# rollback()

connection.rollback()

Purpose:

Undo changes if an error occurs.

Think:

Undo button.

---

# fetchone()

Returns:

One row

or

None

Example:

(101, "Raman", 95)

Use when expecting only one result.

---

# fetchall()

Returns:

List of tuples.

Example:

[
(101, "Raman", 95),
(102, "Aman", 88)
]

Use when expecting multiple rows.

---

# WHERE

WHERE filters rows.

Example:

SELECT * FROM students
WHERE roll = 101;

Without WHERE:

UPDATE changes every row.

DELETE removes every row.

Always check WHERE before UPDATE or DELETE.

---

# Primary Key

Primary Key must be unique.

In SchoolOS:

Roll Number = Primary Key.

Two students cannot have the same roll number.

---

# SQL Commands Learned

INSERT

SELECT

UPDATE

DELETE

WHERE

---

# Project Structure

main.py

↓

student.py

↓

database.py

main.py controls the program.

student.py contains business logic.

database.py connects to MySQL.

---

# Common Errors

Duplicate entry

Reason:

Roll number already exists.

Fix:

Check first or handle IntegrityError.

---

ModuleNotFoundError

Reason:

mysql-connector-python not installed
or wrong Python interpreter.

---

# Biggest Learning

Python does not store the data.

MySQL stores the data.

Python only sends SQL queries to MySQL.
