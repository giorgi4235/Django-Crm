import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'Revazizo1'
	)

# prepare a cursore object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE main_db")

print('database was created')