from database.connection import get_connection as conn
from app import app


@app.route('/')
@app.route('/index')
def index():
    connection = conn()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("EXPLAIN service_station.`Auto`;")
            data = cursor.fetchone()
            return str(data)
