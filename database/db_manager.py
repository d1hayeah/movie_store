import sqlite3
from config import DB_NAME

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            movie_id INTEGER PRIMARY KEY,
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
            client_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suppliers (
            supplier_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            contact_info TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
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