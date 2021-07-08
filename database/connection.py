import pymysql


def get_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        charset="utf8mb4",
        port=3306,
        db="service_station",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
