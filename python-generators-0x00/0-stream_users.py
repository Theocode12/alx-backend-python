#!/bin/python3


from seed  import connect_to_prodev

def stream_users():
    conn = connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data;")
    row = cursor.fetchone()
    while row:
        yield row
        row = cursor.fetchone()

if __name__ == "__main__":
    stream_users()
