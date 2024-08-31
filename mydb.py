import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root@123',
    auth_plugin='mysql_native_password'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("ALL DONE!")