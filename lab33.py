import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hello"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Ram", "Patan")
val = ("Sam", "Ktm")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")