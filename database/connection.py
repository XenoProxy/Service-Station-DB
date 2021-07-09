import mysql.connector
import pymysql


def get_connection():
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        port=3306,
        db="service_station",
        ssl_disabled=True,
    )
    return connection
