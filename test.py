import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="hoang",
  password="123456789",
  auth_plugin='mysql_native_password'
)

print(mydb)