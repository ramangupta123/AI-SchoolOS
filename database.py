# Import the MySQL connector library.
# This library allows Python to communicate with a MySQL server.
import mysql.connector


print("Connecting to MySQL...")


# Create a connection with the MySQL server.
# Think of this as opening a phone call with MySQL.
connection = mysql.connector.connect(

    # Where is the MySQL server?
    # "localhost" means it is running on THIS laptop.
    host="localhost",

    # Username used to log into MySQL.
    user="root",

    # Password for the MySQL user.
    # Leave it empty because your root user currently has no password.
    password="",

    # Which database should Python use after connecting?
    database="schoolos"
)


print("✅ Connected Successfully!")


# A cursor is like a messenger.
#
# Python itself cannot execute SQL.
#
# Instead, Python tells the cursor:
#
# "Execute this SQL query."
#
# The cursor sends that query to MySQL.
cursor = connection.cursor()


print("✅ Cursor Created Successfully!")
