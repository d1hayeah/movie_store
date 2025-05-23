from database.db_manager import get_connection

class Order:
    def __init__(self, order_id=None, movie_id=None, client_id=None, sale_date=None, quantity=None, total_price=None, employee_id=None):
        self.order_id = order_id
        self.movie_id = movie_id
        self.client_id = client_id
        self.sale_date = sale_date
        self.quantity = quantity
        self.total_price = total_price
        self.employee_id = employee_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.order_id is None:
            cursor.execute('''
                INSERT INTO orders(movie_id, client_id, sale_date, quantity, total_price, employee_id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.movie_id, self.client_id, self.sale_date, self.quantity, self.total_price, self.employee_id))
            self.order_id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE orders SET movie_id=?, client_id=?, sale_date=?, quantity=?, total_price=?, employee_id=?
                WHERE order_id=?
            ''', (self.movie_id, self.client_id, self.sale_date, self.quantity, self.total_price, self.employee_id, self.order_id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.order_id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM orders WHERE order_id=?", (self.order_id,))
            conn.commit()
            conn.close()

def get_all_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    conn.close()
    return [ Order(
        order_id=row[0],
        movie_id=row[1],
        client_id=row[2],
        sale_date=row[3],
        quantity=row[4],
        total_price=row[5],
        employee_id=row[6]
    ) for row in rows ]

def get_order_by_id(order_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Order(
            order_id=row[0],
            movie_id=row[1],
            client_id=row[2],
            sale_date=row[3],
            quantity=row[4],
            total_price=row[5],
            employee_id=row[6]
        )
    return None