import time
import sqlite3 
import functools


query_cache = {}

"""your code goes here"""
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect('users.db')
        result = func(connection, *args, **kwargs)
        return result
    return wrapper

def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get('query')
        if query not in query_cache:
            query_cache[query] = func(conn, query)
        return query_cache[query]
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")