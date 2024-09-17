import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hello"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Ktm'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")