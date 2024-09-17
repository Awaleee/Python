import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hello"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Butwal' WHERE address = 'Patan'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")