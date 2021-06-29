from connection import get_connection as connection


def sp_create_user():
    conn = connection()
    cursor = conn.cursor()
    sp = """DELIMITER $$
            CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
                IN p_name VARCHAR(20),
              IN p_username VARCHAR(20),
                IN p_password VARCHAR(20)
            )
            BEGIN
                if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
                 
                    select 'Username Exists !!';
                 
                ELSE
                 
                    insert into tbl_user
                    (
                        user_name,
                        user_username,
                        user_password
                    )
                    values
                    (
                        p_name,
                        p_username,
                        p_password
                    );
                 
                END IF;
            END$$
            DELIMITER ;"""
    return cursor.execute(sp)
