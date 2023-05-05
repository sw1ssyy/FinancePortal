import mysql.connector
""" File used to store the Databases Details and Connections"""
DB = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Newport2012.'
)

CURSOR = DB.cursor()

CURSOR.execute("CREATE DATABASE finance")
print('Database Created')