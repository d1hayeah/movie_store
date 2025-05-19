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
            supplier_id INTEGER,
            title TEXT NOT NULL,
            director TEXT NOT NULL,
            genre TEXT,
            actors TEXT,
            format TEXT,
            release_year INTEGER,
            stock_quantity INTEGER,
            price INTEGER,
            FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id)
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
            phone TEXT,
            email TEXT
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
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rentals (
            rental_id INTEGER PRIMARY KEY,
            client_id INTEGER NOT NULL,
            movie_id INTEGER NOT NULL,
            rental_date DATE NOT NULL,
            return_date DATE,
            rental_price INTEGER,  
            FOREIGN KEY(client_id) REFERENCES clients(client_id),
            FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            position TEXT NOT NULL,
        )
    ''')


    conn.commit()
    conn.close()