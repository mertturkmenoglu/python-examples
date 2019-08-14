import sqlite3

if __name__ == '__main__':
    db_connection = sqlite3.connect('my_data.db')

    db_connection.execute('''CREATE TABLE SCHOOL
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             ADDRESS        CHAR(50),
             POINTS         REAL);''')

    print("Table created successfully")

    db_connection.close()
