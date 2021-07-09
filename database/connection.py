import pymysql


def get_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        charset="utf8mb4",
        port=3306,
        db="service_station"
    )
    return connection
