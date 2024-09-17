import csv
import mysql.connector

def insert_name(name):
    conn = mysql.connector.connect(
        host='localhost',
        database='hello',
        user='root',
        password=''
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()

def read_csv_and_insert(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            name = row['Name']
            if name.startswith('S') or name.startswith('J'):
                insert_name(name)
                print(f"Inserted: {name}")

# Example usage
read_csv_and_insert('students.csv')
