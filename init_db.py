import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql', mode='r') as file:
    connection.executescript(file.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('First Post', 'Content for the first post'))

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Second Post', 'Content for the second post'))

connection.commit()
connection.close()
