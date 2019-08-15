import sqlite3

if __name__ == '__main__':
    db_connection = sqlite3.connect('my_data.db')
    cursor = db_connection.execute("SELECT * FROM SCHOOL")

    for e in cursor:
        print(e)

    db_connection.close()
