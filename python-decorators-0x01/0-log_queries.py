import sqlite3
import functools
from datetime import datetime
import logging

# Proper logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""

def log_queries(func):
   @functools.wraps(func)
   def wrapper(*args, **kwargs):
        query = kwargs.get("query")
        if query:
            logging.info(f"Executing query: {query}")
            print(f"{datetime.now}, {query}")
        return func(*args, **kwargs)
   return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
