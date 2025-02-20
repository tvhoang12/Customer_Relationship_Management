import mysql.connector

dataBase = mysql.connector.connect(
    host = "127.0.0.1",
    user = "hoang",
    passwd = "123456789",
    database = "crm",
    auth_plugin='mysql_native_password'
)

#prepare a cursor object
cursor = dataBase.cursor()

#create a database
cursor.execute("select 1")

print("Database created successfully")