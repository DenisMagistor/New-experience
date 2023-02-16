# Create table
def create_table():
    import sqlite3
    with sqlite3.connect('data.db') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS DaTa(
        name varchar(10),
        age INTEGER,
        password text
        )''')


# Add data for BD
def add_data(func):
    import sqlite3
    with sqlite3.connect('data.db') as db:
        cursor = db.cursor()
        cursor.executemany('INSERT INTO DaTa VALUES (?, ?, ?)', func)


# Generation data for use in BD
def generator_data(n: int = 10000):
    from faker import Faker
    from random import randint
    from time import time
    from rich import print

    list_ = []
    checker_2 = n
    checker = 0
    start_ = time()

    while n > 0:
        start = time()
        list_.append([Faker().name(), randint(0, 100), Faker().password(), ])
        n -= 1
        checker += 1
        print(f'Подготовлена запись\t{checker}/{checker_2}\tTime:{round(time() - start, 3)}')

    print(f'\n[bold red]Time: {round(time() - start_, 3)}')
    return list_