from database.db_manager import get_connection

class Films:
    def __init__(self, movie_id=None, supplier_id=None, title=None, director=None, genre=None, actors=None, format=None, release_year=None, stock_quantity=None, price=None):
        self.movie_id = movie_id
        self.supplier_id = supplier_id
        self.title = title
        self.director = director
        self.genre = genre
        self.actors = actors
        self.format = format        
        self.release_year = release_year
        self.stock_quantity = stock_quantity
        self.price = price
        
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.movie_id is None:
            cursor.execute("""INSERT INTO movies (supplier_id, title, director, genre, actors, format, release_year, stock_quantity, price)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                            (self.supplier_id, self.title, self.director, self.genre, self.actors, self.format, self.release_year, self.stock_quantity, self.price))
            self.movie_id = cursor.lastrowid
        else:
            cursor.execute("""UPDATE movies SET supplier_id = ?, title = ?, director = ?, genre = ?, actors = ?, format = ?, release_year = ?, stock_quantity = ?, price = ?
                                WHERE movie_id = ?""", 
                                (self.supplier_id, self.title, self.director, self.genre, self.actors, self.format, self.release_year, self.stock_quantity, self.price, self.movie_id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.movie_id is not None:
            cursor.execute("DELETE FROM movies WHERE movie_id = ?", (self.movie_id,))
        conn.commit()
        conn.close()


def get_all_movies():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT movie_id, supplier_id, title, director, genre, actors, format, release_year, stock_quantity, price FROM movies")
    rows = cursor.fetchall()
    conn.close()
    return [ Films(
        movie_id=row[0],
        supplier_id=row[1],
        title=row[2],
        director=row[3],
        genre=row[4],
        actors=row[5],
        format=row[6],
        release_year=row[7],
        stock_quantity=row[8],
        price=row[9]
    ) for row in rows ]

def get_movie_by_id(movie_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT movie_id, supplier_id, title, director, genre, actors, format, release_year, stock_quantity, price FROM movies WHERE movie_id=?", (movie_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Films(
            movie_id=row[0],
            supplier_id=row[1],
            title=row[2],
            director=row[3],
            genre=row[4],
            actors=row[5],
            format=row[6],
            release_year=row[7],
            stock_quantity=row[8],
            price=row[9]
        )
    return None

