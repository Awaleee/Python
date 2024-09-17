import mysql.connector
mydb = mysql.connector.connect( 
    host="localhost", 
    user="root",
    password="",
    database="hello"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = %s"
adr=("Patan", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
