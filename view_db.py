import sqlite3

# Connect to the database
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Query the data
c.execute('SELECT * FROM tasks')
tasks = c.fetchall()

# Print the data
for task in tasks:
    print(task)

# Close the connection
conn.close()
