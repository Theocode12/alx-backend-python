import sqlite3 
import functools
from sqlite3 import Connection

"""your code goes here"""
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect('users.db')
        result = func(connection, *args, **kwargs)
        return result
    return wrapper

def transactional(func):
    @functools.wraps(func)
    def wrapper(connection, *args, **kwargs):
        connection: Connection = connection
        if connection:
            try:
                func(connection, *args, **kwargs)
                connection.commit()
            except Exception as e:
                connection.rollback()
                print(f"exception occured {str(e)}")
            finally:
                connection.close()
    return wrapper




@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')