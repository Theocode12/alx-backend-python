#!/usr/bin/python3
seed = __import__('seed')

def stream_users_in_batches(batch_size):
    connection = seed.connect_to_prodev()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data LIMIT %s", (batch_size,))
        for row in cursor.fetchall():
            yield row

def batch_processing(batch_size):
    for row in stream_users_in_batches(batch_size):
        if row.get('age') > 25:
            print(row)