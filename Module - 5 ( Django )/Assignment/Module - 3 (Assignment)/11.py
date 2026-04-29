import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Mohit", 21))
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Rahul", 22))

conn.commit()

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

conn.close()