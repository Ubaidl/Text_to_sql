import sqlite3

# Create a new database or connect to an existing one
connection = sqlite3.connect("STUDENT.db")

# Create a cursor
cursor = connection.cursor()

# Create a table
table_info = """
CREATE TABLE IF NOT EXISTS Student(
    Name VARCHAR(25),
    Class VARCHAR(25),
    Section VARCHAR(25),
    Marks INT
)
"""
cursor.execute(table_info)

# Insert some records (one by one)
cursor.execute("INSERT INTO Student VALUES ('ubaid', 'ml', 'A', 90)")
cursor.execute("INSERT INTO Student VALUES ('sajad', 'dl', 'B', 80)")
cursor.execute("INSERT INTO Student VALUES ('mubashir', 'C++', 'D', 70)")

# Display all records
data = cursor.execute("SELECT * FROM Student")
for row in data:
    print(row)

# Commit changes and close the connection
connection.commit()
connection.close()
