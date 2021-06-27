from database.connection import mysql
from app import app


@app.route('/')
@app.route('/index')
def index():
    # conn = mysql.connect()
    # cursor = conn.cursor()
    # cursor.execute("SELECT * service_station.`Auto`;")
    # data = cursor.fetchall()
    return "successful connection!"
