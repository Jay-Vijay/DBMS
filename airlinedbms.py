import mysql.connector

# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="jay"
)

cursor = conn.cursor()

# Create the students table
cursor.execute("""
CREATE TABLE airlines (
    airline_id INT PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255)
);
""")

# Function to insert data
def insert_airline(airline_id, name, country):
    insert_query = "INSERT INTO airlines (airline_id, name, country) VALUES (%s, %s, %s)"
    values = (airline_id, name, country)
    cursor.execute(insert_query, values)
    conn.commit()
    print("Airline inserted successfully")

# Function to update data
def update_airline(airline_id, new_name, new_country):
    update_query = "UPDATE airlines SET name = %s, country = %s WHERE airline_id = %s"
    values = (new_name, new_country, airline_id)
    cursor.execute(update_query, values)
    conn.commit()
    print("Airline updated successfully")

# Inserting a new airline
insert_airline(11, "Airline A", "Country A")

# Updating an existing airline
update_airline(231, "Airline B", "Country B")

# Closing the connection
cursor.close()
conn.close()
