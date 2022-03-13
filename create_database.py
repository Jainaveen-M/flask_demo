import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root@123',
)

my_cursor = mydb.cursor()

my_cursor.execute('CREATE DATABASE test_user')

my_cursor.execute('show databases')
for db in my_cursor:
    print(db)