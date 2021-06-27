from database.connection import mysql


connection = mysql.connect()
with connection:
    with connection.cursor() as cursor:
        db_create = """
        CREATE DATABASE IF NOT EXISTS service_station;
        """
        cursor.execute(db_create)
    connection.commit()

    with connection.cursor() as cursor:
        tbl_auto_create = """
            CREATE TABLE IF NOT EXISTS service_station.`Auto` (
            `VIN` VARCHAR(17) NOT NULL,
            `Number` VARCHAR(15) NOT NULL,
            `Brand` VARCHAR(15) NOT NULL,
            `Model` VARCHAR(30) NOT NULL,
            `Make` YEAR NOT NULL,
            PRIMARY KEY(`VIN`)
            )
            """
        cursor.execute(tbl_auto_create)

        tbl_clients_create = """
            CREATE TABLE IF NOT EXISTS service_station.`Clients` (
            `ID` INT AUTO_INCREMENT PRIMARY KEY,
            `Name` VARCHAR(15) NOT NULL,
            `Surname` VARCHAR (20) NOT NULL
            )
            """
        cursor.execute(tbl_clients_create)

        tbl_employees_create = """
            CREATE TABLE IF NOT EXISTS service_station.`Employees` (
            `ID` INT AUTO_INCREMENT PRIMARY KEY,
            `Name` VARCHAR(15) NOT NULL,
            `Surname` VARCHAR (20) NOT NULL,
            `Specialization` VARCHAR(20) NOT NULL,
            `Rank` ENUM('1','2','3','4','5') NOT NULL
            )
            """
        cursor.execute(tbl_employees_create)

        tbl_service_create = """
            CREATE TABLE IF NOT EXISTS service_station.`Service` (
            `ID` INT AUTO_INCREMENT PRIMARY KEY,
            `Name` VARCHAR(15) NOT NULL,
            `Auto` VARCHAR(17) NOT NULL,
            `Owner` INT NOT NULL,
            `Employee` INT NOT NULL,
            `Price` INT NOT NULL,
            `Beginning` DATE NOT NULL,
            `Completion` DATE NOT NULL,
            FOREIGN KEY(`Auto`) REFERENCES `Auto`(`VIN`),
            FOREIGN KEY(`Employee`) REFERENCES `Employees`(`ID`),
            FOREIGN KEY(`Owner`) REFERENCES `Clients`(`ID`)
            )
            """
        cursor.execute(tbl_service_create)
