import mysql.connector

DB = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Newport2012.'
)

CURSOR = DB.cursor()

CURSOR.execute("CREATE DATABASE finance")
print('Database Created')