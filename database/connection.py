import pymysql


def get_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successful connection!")
    return connection
