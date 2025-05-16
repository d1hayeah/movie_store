from database.db_manager import get_connection

class Supplier:
    def __init__(self, supplier_id=None, name=None, contact_info=None):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.supplier_id is None:
            cursor.execute("INSERT INTO suppliers(name, contact_info) VALUES (?, ?)",
                           (self.name, self.contact_info))
            self.supplier_id = cursor.lastrowid
        else:
            cursor.execute("UPDATE suppliers SET name=?, contact_info=? WHERE supplier_id=?",
                           (self.name, self.contact_info, self.supplier_id))
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
    return [Supplier(
        supplier_id=row[0],
        name=row[1],
        contact_info=row[2]
    ) for row in rows]

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
            contact_info=row[2]
        )
    return None