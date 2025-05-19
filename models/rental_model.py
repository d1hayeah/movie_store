from database.db_manager import get_connection

class Rental:
    def __init__(self, rental_id=None, client_id=None, movie_id=None, rental_date=None, return_date=None, rental_price=None):
        self.rental_id = rental_id
        self.client_id = client_id
        self.movie_id = movie_id
        self.rental_date = rental_date
        self.return_date = return_date
        self.rental_price = rental_price

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.rental_id is None:
            cursor.execute("""INSERT INTO rentals (client_id, movie_id, rental_date, return_date, rental_price)
                            VALUES (?, ?, ?, ?, ?)""", 
                            (self.client_id, self.movie_id, self.rental_date, self.return_date, self.rental_price))
            self.rental_id = cursor.lastrowid
        else:
            cursor.execute("""UPDATE rentals SET client_id = ?, movie_id = ?, rental_date = ?, return_date = ?, rental_price = ?
                                WHERE rental_id = ?""", 
                                (self.client_id, self.movie_id, self.rental_date, self.return_date, self.rental_price, self.rental_id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.rental_id is not None:
            cursor.execute("DELETE FROM rentals WHERE rental_id = ?", (self.rental_id,))
        conn.commit()
        conn.close()

def get_all_rentals():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rentals")
    rows = cursor.fetchall()
    conn.close()
    return [ Rental(
        rental_id=row[0],
        client_id=row[1],
        movie_id=row[2],
        rental_date=row[3],
        return_date=row[4],
        rental_price=row[5]
    ) for row in rows ]

def get_rental_by_id(rental_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rentals WHERE rental_id = ?", (rental_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Rental(
            rental_id=row[0],
            client_id=row[1],
            movie_id=row[2],
            rental_date=row[3],
            return_date=row[4],
            rental_price=row[5]
        )
    return None
