import sqlite3

connection = sqlite3.connect("test_table.db")

cursor = connection.cursor()

sql_command = """CREATE TABLE emp ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE);"""

cursor.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (23, "Calvin", "Cruzada", "M", "2014-03-28");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (25, "Daion", "Cruzada", "M", "2012-01-04");"""
cursor.execute(sql_command)

connection.commit()

connection.close()