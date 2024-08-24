import sqlite3 as sq
from random import random

users = [
    ("Daniel", 1, 20),
    ("Michael", 1, 19),
    ("Marina", 2, 21),
    ("Alexander", 1, 18)
]


def open_img(path:str):
    try:
        with open(path, 'rb') as f:
            return f.read()
    except IOError as e:
        print(e)
        return False


with sq.connect('test.db') as conn:
    conn.row_factory = sq.Row
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id_pk integer PRIMARY KEY AUTOINCREMENT,
    Name Text NOT NULL,
    sex Integer NOT NULL,
    age Integer
    )""")

    cur.execute("PRAGMA table_info(users);")
    columns = [column[1] for column in cur.fetchall()]

    if 'ava' not in columns:
        cur.execute("""ALTER TABLE users 
        ADD ava BLOB """)

    img = open_img('/Users/macbook/Desktop/8ae1a2c256428e0df54a21cf453aa9f4.jpeg')

    if img:
        binary = sq.Binary(img)
        cur.execute("""UPDATE users
        SET ava = ?
        WHERE name = 'Daniel'""", (binary,) )

