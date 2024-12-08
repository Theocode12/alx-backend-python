import time
import sqlite3 
import functools

#### paste your with_db_decorator here

""" your code goes here"""
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect('users.db')
        result = func(connection, *args, **kwargs)
        return result
    return wrapper

def retry_on_failure(retries, delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            print("In retries")
            if not conn:
                conn = next(
                    (sqlite3.connect('users.db') for _ in range(retries) if (time.sleep(delay) or sqlite3.connect('users.db'))), 
                    None)
            return func(conn, *args, **kwargs)
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)