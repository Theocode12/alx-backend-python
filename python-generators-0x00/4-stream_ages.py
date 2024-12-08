#!/usr/bin/python3
seed = __import__('seed')

def stream_user_ages():
    connection = seed.connect_to_prodev()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT age FROM user_data")
        for row in cursor.fetchall():
            yield row.get('age')


def main():
    import statistics
    avg = statistics.fmean(stream_user_ages())
    print(f"Average age of users: {avg}")

if __name__ == '__main__':
    main()