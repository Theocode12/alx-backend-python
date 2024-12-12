#!/usr/bin/python3
from mysql.connector import connect


# Database connection details
host = "127.0.0.1"  # localhost mapped from the container
port = 3306         # Port mapped from the container
user = "root"       # MySQL root user
password = "root"   # Root password as per your compose file
database = None     # Specify a database name if required (e.g., "testdb")

class ExecuteQuery:
    def __init__(self, query, *params):
        self.connection = None
        self.query = f"{query}".replace('?', '{}').format(*params)

    def __enter__(self):
        self.connection = connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database="ALX_prodev"
        )
        cursor = self.connection.cursor()
        cursor.execute(self.query)
        return cursor.fetchall()

    def __exit__(self, type, value, traceback):
        self.connection.close()

if __name__ == "__main__":
    with ExecuteQuery("SELECT * FROM users WHERE age > ? LIMIT ?", 25, 5) as result:
        print(result)