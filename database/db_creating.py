from connection import get_connection as conn


connection = conn()
with connection:
    with connection.cursor() as cursor:
        db_create = """
        CREATE DATABASE IF NOT EXISTS service_station;
        """
        cursor.execute(db_create)
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        tbl_create = """
            CREATE TABLE IF NOT EXISTS service_station.`Auto` (
            `VIN` VARCHAR(17) NOT NULL,
            `Number` VARCHAR(15) NOT NULL,
            `Brand` VARCHAR(15),
            `Model` VARCHAR(30),
            `Make` YEAR,
            PRIMARY KEY(`VIN`)
            )
            """
        cursor.execute(tbl_create)
