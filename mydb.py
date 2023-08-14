import mysql.connector

#creating a db connection
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'muchirinjeri3210@gmail.com',
    passwd = 'HNE-i76NXNE,i+E',
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#creating a database
cursorObject.execute("CREATE BATABASE recordingg")

print("All Done!")
