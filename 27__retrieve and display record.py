import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # your username
    password="your_password",
    database="testdb"
)

cursor = conn.cursor()

# Retrieve records
cursor.execute("SELECT * FROM students")

# Fetch all rows
rows = cursor.fetchall()

# Display records
print("Student Records:\n")
for row in rows:
    print("ID:", row[0], "Name:", row[1], "Age:", row[2])

# Close connection
cursor.close()
conn.close()
