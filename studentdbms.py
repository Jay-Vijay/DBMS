import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="jay"
)

cursor = conn.cursor()

# Function to insert a student
def insert_student(student_id, name, age, grade):
    insert_query = "INSERT INTO students (student_id, name, age, grade) VALUES (%s, %s, %s, %s)"
    values = (student_id, name, age, grade)
    cursor.execute(insert_query, values)
    conn.commit()
    print("Student inserted successfully")

# Function to update student grade
def update_student_grade(student_id, new_grade):
    update_query = "UPDATE students SET grade = %s WHERE student_id = %s"
    values = (new_grade, student_id)
    cursor.execute(update_query, values)
    conn.commit()
    print("Student grade updated successfully")

# Create the students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    grade VARCHAR(50)
)
""")

# Inserting a new student
insert_student(1, "Alice Johnson", 14, "8th Grade")

# Updating an existing student's grade
update_student_grade(1, "9th Grade")

# Closing the connection
cursor.close()
conn.close()
