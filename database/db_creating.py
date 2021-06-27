import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    charset='cp1251',
)
print("successful connection!")

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE python_db;")
mycursor.close()