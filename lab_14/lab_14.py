import sqlite3

connecton = sqlite3.connect('my_database.sql')
cursor = connection.cursor()

cursor.execute('Select * FROM Users')
users = cursor.fetchall()

for user in users:
    print(user)

conection.close()