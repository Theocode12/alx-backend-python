#!/bin/python3


from seed  import connect_to_prodev

def stream_users():
    conn = connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data;")
    row = cursor.fetchone()
    while row := cursor.fetchone():
        yield row

if __name__ == "__main__":
    i = 0
    for u in stream_users():
        print(u)
        i += 1
        if i == 5:
            break
