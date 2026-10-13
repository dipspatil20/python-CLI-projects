import sqlite3
from models.customers import Customer
from models.menu import MenuItem

class DBManager:
    def __init__(self, db_path='dominos.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT, email TEXT UNIQUE, password TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS menu_items (
                            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT, price REAL, description TEXT)''')
        self.conn.commit()

    def add_customer(self, name, email, password):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO customers (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        self.conn.commit()

    def get_customer_by_email(self, email):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE email=?", (email,))
        row = cursor.fetchone()
        if row:
            return Customer(*row)
        return None

    def add_menu_item(self, name, price, description):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO menu_items (name, price, description) VALUES (?, ?, ?)", (name, price, description))
        self.conn.commit()

    def get_all_menu_items(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM menu_items")
        rows = cursor.fetchall()
        return [MenuItem(*row) for row in rows]
