from connection import get_connection as conn


connection = conn()
with connection:
    with connection.cursor() as cursor:
        db_create = "CREATE DATABASE %s;"
        cursor.execute(db_create, "service_station")
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)