from modules import *

# Get data from BD
def get_data():
    import sqlite3
    with sqlite3.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM DaTa')
        names = cursor.fetchall()

        need_data = []
        for row in names:
            need_data.append(row)

        return need_data


# Delete data
def deleted_data_from_bd():
    import sqlite3
    with sqlite3.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute('DELETE FROM DaTa')