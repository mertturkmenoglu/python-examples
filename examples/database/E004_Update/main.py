import sqlite3

if __name__ == '__main__':
    db_connection = sqlite3.connect('my_data.db')
    db_connection.execute("UPDATE SCHOOL SET AGE=21 WHERE ID=1")
    db_connection.commit()

    cursor = db_connection.execute("SELECT * FROM SCHOOL")

    for e in cursor:
        print(e)

    db_connection.close()
