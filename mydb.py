import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Password1234!'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE iridescentreef")

print("All Done!")