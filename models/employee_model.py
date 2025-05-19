from database.db_manager import get_connection

class Employee:
    def __init__(self, employee_id=None, first_name=None, last_name=None, position=None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.employee_id is None:
            cursor.execute("""INSERT INTO employees (first_name, last_name, position)
                            VALUES (?, ?, ?)""", 
                            (self.first_name, self.last_name, self.position))
            self.employee_id = cursor.lastrowid
        else:
            cursor.execute("""UPDATE employees SET first_name = ?, last_name = ?, position = ?
                                WHERE employee_id = ?""", 
                                (self.first_name, self.last_name, self.position, self.employee_id))
        conn.commit()
        conn.close()

    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.employee_id is not None:
            cursor.execute("DELETE FROM employees WHERE employee_id = ?", (self.employee_id,))
        conn.commit()
        conn.close()

def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return [ Employee(
        employee_id=row[0],
        first_name=row[1],
        last_name=row[2],
        position=row[3]
    ) for row in rows ]

def get_employee_by_id(employee_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Employee(
            employee_id=row[0],
            first_name=row[1],
            last_name=row[2],
            position=row[3]
        )
    return None
