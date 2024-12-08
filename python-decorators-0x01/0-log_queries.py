import sqlite3
import functools

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""

def log_queries(func):
   @functools.wraps(func)
   def wrapper(*args, **kwargs):
      print(kwargs.get('query'))
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
print(users)

from sqlite3 import Connection
## create user
def connect(func):
    def wrapper(arg):
        conn = sqlite3.connect('users.db')
        func(arg, conn)
        result = conn.execute("SELECT * FROM users")
        print(result.fetchone())
        conn.commit()
        conn.close()
    return wrapper

@connect
def db_query(query, connection: Connection):
    connection.cursor().execute(query)
    # pass

# db_query("CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY , name VARCHAR(40), email VARCHAR(40) UNIQUE, age INT)")

# db_query("""INSERT INTO users (name, age, email)VALUES ('Alice', 30, 'Bob@example.com')""")