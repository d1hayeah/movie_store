import sqlite3
from config import DB_NAME

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            director TEXT NOT NULL,
            genre TEXT,
            actors TEXT,
            format TEXT,
            release_year INTEGER,
            stock_quantity INTEGER,
            price INTEGER
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_info TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER,
            client_id INTEGER,
            sale_date DATE,
            type TEXT,
            rental_date DATE,
            return_date DATE,
            quantity INTEGER,
            total_price INTEGER,
            FOREIGN KEY(movie_id) REFERENCES movies(id),
            FOREIGN KEY(client_id) REFERENCES clients(id)
        )
    ''')



    conn.commit()
    conn.close()