import sqlite3

if __name__ == '__main__':
    db_connection = sqlite3.connect('my_data.db')
    db_connection.execute("INSERT INTO SCHOOL (ID, NAME, AGE, ADDRESS, POINTS) \
                          VALUES (1, 'Emily', 35, 'London', 100.0)")
    db_connection.execute("INSERT INTO SCHOOL (ID, NAME, AGE, ADDRESS, POINTS) \
                          VALUES (2, 'Diana', 42, 'Greece', 95.3)")
    db_connection.commit()

    print('Committed')
    db_connection.close()
