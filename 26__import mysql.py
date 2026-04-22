import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # your MySQL username
    password="avinash$$123",
    database="testdb"     # make sure this DB exists
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

print("Table created successfully")

# Insert records
sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
values = [
    ("Rahul", 20),
    ("Priya", 22),
    ("Amit", 19)
]

cursor.executemany(sql, values)

# Save changes
conn.commit()

print(cursor.rowcount, "records inserted")

# Display data
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()