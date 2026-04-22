import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="avinash$$123",
    database="testdb"
)

cursor = conn.cursor()

# UPDATE
cursor.execute("UPDATE students SET age=23 WHERE name='Priya'")
conn.commit()

# DELETE
cursor.execute("DELETE FROM students WHERE name='Amit'")
conn.commit()

# DISPLAY
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
7
