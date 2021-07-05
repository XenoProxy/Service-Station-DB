from connection import get_connection as connection


def sp_create_user():
    conn = connection()
    cursor = conn.cursor()
    sp = """DELIMITER $$
            CREATE DEFINER=`dispatcher`@`localhost` PROCEDURE `sp_createUser`(
                IN username VARCHAR(20),
                IN password VARCHAR(20)
            )
            BEGIN
                if (
                    select exists (
                        select 1 from service_station.`tbl_user` where
                        user_username = username
                    )
                ) THEN                 
                    select 'Username Exists !!';                 
                ELSE                 
                    insert into service_station.`tbl_user` (
                    user_username, user_password) values (
                    username, password);                 
                END IF;
            END$$
            DELIMITER ;"""
    return cursor.execute(sp)
