#!/usr/bin/python3
seed = __import__('seed')

def stream_users():
    connection = seed.connect_to_prodev()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        for row in cursor.fetchall():
            yield row
