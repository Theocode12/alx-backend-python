#!/usr/bin/python3
from mysql.connector import connect


# Database connection details
host = "127.0.0.1"  # localhost mapped from the container
port = 3306         # Port mapped from the container
user = "root"       # MySQL root user
password = "root"   # Root password as per your compose file
database = None     # Specify a database name if required (e.g., "testdb")

class DatabaseConnection:
    def __init__(self):
        self.connection = None
    
    def __enter__(self):
        self.connection = connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database="ALX_prodev"
        )
        return self.connection

    def __exit__(self, type, value, traceback):
        if self.connection:
            self.connection.close()


if __name__ == "__main__":
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(users)