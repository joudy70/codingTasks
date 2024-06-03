
# To create database using SQLite, import sqlite3 module 

import sqlite3


# Define a database in the name of 'student.db' with sqlite3.connect() function.
# This function connects to the databsae or creates it if it doesn't exist.

db = sqlite3.connect('student.db')


# Create a cursor object to make changes to the database.

cursor = db.cursor()



# Create a database with three columns.
# Check if the table doesn't exist before.

cursor.execute('''
               CREATE TABLE IF NOT EXISTS python_programming (id INTEGER PRIMARY KEY,
                name TEXT, grade INTEGER)
               ''')



# Create a list of data and insert them into the table.
# Use commit statement to finalise the changes.

data_list = [
    (55, 'Carl Davis', 61), 
    (66, 'Denis Fredrickson', 88), 
    (77, 'Jane Richards', 78), 
    (12, 'Peyton Sawyer', 45), 
    (2, 'Lucas Brook', 99)
    ]

cursor.executemany("INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)", data_list)
db.commit()



# Select records with a grade between 60 and 80.

cursor.execute("SELECT * FROM python_programming WHERE grade>60 and grade<80")




#  Change Carl Davis’s grade to 65.

cursor.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")



# Delete Dennis Fredrickson’s row.

cursor.execute("DELETE FROM python_programming WHERE name = 'Denis Fredrickson'")



#Change the grade of all students with an id greater than 55 to a grade of 80.

cursor.execute("UPDATE python_programming SET grade = 80 WHERE id > 55")




# Use commit statement to finalise the changes.

db.commit()



# Close database to protect the datas.
db.close()