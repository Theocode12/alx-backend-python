#!/usr/bin/python3
from mysql.connector import connect
import csv
from uuid import uuid4


# Database connection details
host = "127.0.0.1"  # localhost mapped from the container
port = 3306         # Port mapped from the container
user = "root"       # MySQL root user
password = "root"   # Root password as per your compose file
database = None     # Specify a database name if required (e.g., "testdb")


def connect_db() :
    return connect(
        host=host,
        port=port,
        user=user,
        password=password,
    )

def create_database(connection):
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")

def connect_to_prodev():
    return connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database="ALX_prodev"
    )

def create_table(connection):
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS user_data")
        cursor.execute("CREATE TABLE IF NOT EXISTS user_data ( user_id VARCHAR(36) PRIMARY KEY , name VARCHAR(40), email VARCHAR(40) UNIQUE, age INT)")

def insert_data(connection, csv_file):
    with connection.cursor() as cursor:
        with open(csv_file) as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                insert_statement = f"""INSERT INTO user_data (user_id, name, email, age) VALUES ("{str(uuid4())}", "{row.get("name")}", "{row.get("email")}", "{row.get('age')}")"""
                cursor.execute(insert_statement) 
    connection.commit()
