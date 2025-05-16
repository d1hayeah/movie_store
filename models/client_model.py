from database.db_manager import get_connection

class Client:
    def __init__(self, client_id=None, name=None, phone=None, email=None):
        self.client_id = client_id
        self.name = name
        self.phone = phone
        self.email = email

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.client_id is None:
            cursor.execute("INSERT INTO clients(name, phone, email) VALUES (?, ?, ?)",
                           (self.name, self.phone, self.email))
            self.client_id = cursor.lastrowid
        else:
            cursor.execute("UPDATE clients SET name=?, phone=?, email=? WHERE client_id=?",
                           (self.name, self.phone, self.email, self.client_id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.client_id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clients WHERE client_id=?", (self.client_id,))
            conn.commit()
            conn.close()

def get_all_clients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    rows = cursor.fetchall()
    conn.close()
    return [Client(
        client_id=row[0],
        name=row[1],
        phone=row[2],
        email=row[3]
    ) for row in rows]

def get_client_by_id(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE client_id=?", (client_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Client(
            client_id=row[0],
            name=row[1],
            phone=row[2],
            email=row[3]
        )
    return None