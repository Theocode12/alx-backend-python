#!/bin/python3


import mysql.connector
import csv

# this function assumes you have ran the create_prodev_user.sql
# script
def connect_db(user = "prodev", password = 0, host = "localhost", db = ""):
     try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=f"{password}",
            database=db # an empty db ie ""  connects to mysql db
        )
        
     except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection = None 
     finally:
        return connection


def create_database(connection, db_name = "ALX_prodev"):
    create_db_stmt = f"""
        CREATE DATABASE IF NOT EXISTS {db_name};
    """

    conn = connect_db()
    if not conn:
        raise Exception(f"Failed to create datbase {db_name}")
    cursor = conn.cursor()

    cursor.execute(create_db_stmt)
    conn.close()
    cursor.close()

def connect_to_prodev():
    return connect_db(db = "ALX_prodev")

def create_table(connection):
    create_user_table_stmt = """
            CREATE TABLE IF NOT EXISTS  user_data (
                user_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(3,0) NOT NULL,
                INDEX (user_id)
            );
            """
    cursor = connection.cursor()
    cursor.execute(create_user_table_stmt)
    cursor.close()

def insert_data(connection, data_path):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM user_data;")
    count = cursor.fetchone()[0]
    if count == 0:
        insert_query = """
                INSERT INTO user_data (name, email, age)
                VALUES (%s, %s, %s);
                """

        data = extract_csv_from_path(data_path)
        cursor.executemany(insert_query, data)

        connection.commit()

def extract_csv_from_path(file_path):
    data = []

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            row_index = 0
            for row in csv_reader:
                if row_index > 0:
                    row[-1] = int(row[-1])
                    data.append(row)
                row_index += 1
        return data

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"Error: {e}")

    return []

if __name__ == "__main__":
    create_database(connect_db())  
    create_table(connect_to_prodev())
    insert_data(connect_to_prodev(), "user_data.csv")
