import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect(r"C:\Users\shuai.ruan\djangogirls\db.sqlite3")

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM db.sqlite3")

# Fetch data
rows = cursor.fetchall()

# Iterate over the rows
for row in rows:
    print(row)

# Close the connection
conn.close()
