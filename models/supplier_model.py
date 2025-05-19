from database.db_manager import get_connection

class Supplier:
    def __init__(self, supplier_id=None, name=None, phone=None, email=None):
        self.supplier_id = supplier_id
        self.name = name
        self.phone = phone
        self.email = email

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.supplier_id is None:
            cursor.execute("INSERT INTO suppliers(name, phone, email) VALUES (?, ?, ?)",
                           (self.name, self.phone, self.email))
            self.supplier_id = cursor.lastrowid
        else:
            cursor.execute("UPDATE suppliers SET name=?, phone=?, email=? WHERE supplier_id=?",
                           (self.name, self.phone, self.email, self.supplier_id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.supplier_id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM suppliers WHERE supplier_id=?", (self.supplier_id,))
            conn.commit()
            conn.close()

def get_all_suppliers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM suppliers")
    rows = cursor.fetchall()
    conn.close()
    return [ Supplier(
        supplier_id=row[0],
        name=row[1],
        phone=row[2],
        email=row[3]
    ) for row in rows ]

def get_supplier_by_id(supplier_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM suppliers WHERE supplier_id=?", (supplier_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Supplier(
            supplier_id=row[0],
            name=row[1],
            phone=row[2],
            email=row[3]
        )
    return None