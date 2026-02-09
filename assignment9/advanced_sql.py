import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "db", "lesson.db"))

def print_rows(cursor):
    for row in cursor.fetchall():
        print(row)

def populate_database(conn):
    """Create tables and insert sample data if database is empty"""
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price REAL NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        employee_id INTEGER NOT NULL,
        order_date TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS line_items (
        line_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY(order_id) REFERENCES orders(order_id),
        FOREIGN KEY(product_id) REFERENCES products(product_id)
    );
    """)

    cur.execute("SELECT COUNT(*) FROM customers;")
    if cur.fetchone()[0] > 0:
        print("Database already populated.")
        return

    cur.executemany("INSERT INTO customers (customer_name) VALUES (?)",
                    [("Perez and Sons",), ("Global Corp",), ("Alpha Industries",)])

    cur.executemany("INSERT INTO employees (first_name, last_name) VALUES (?, ?)",
                    [("Miranda", "Harris"), ("John", "Doe"), ("Jane", "Smith")])

    cur.executemany("INSERT INTO products (product_name, price) VALUES (?, ?)",
                    [("Product A", 5.0), ("Product B", 7.5), ("Product C", 10.0),
                     ("Product D", 3.5), ("Product E", 12.0), ("Product F", 8.0)])

    cur.executemany("INSERT INTO orders (customer_id, employee_id) VALUES (?, ?)",
                    [(1,1),(2,2),(3,3),(1,1),(2,2)])

    cur.executemany("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
                    [(1,1,2),(1,2,1),(2,3,5),(2,4,2),(3,5,1),
                     (3,6,3),(4,1,4),(4,3,2),(5,2,6),(5,4,1)])

    conn.commit()
    print("Database has been populated successfully!")

def main():
    print("Opening database:", DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    populate_database(conn)

    print("\nTASK 1: Total price of first 5 orders")
    cursor.execute("""
        SELECT
            o.order_id,
            SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
    """)
    print_rows(cursor)

    print("\nTASK 2: Average order price per customer")
    cursor.execute("""
        SELECT
            c.customer_name,
            AVG(order_totals.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
            SELECT
                o.customer_id AS customer_id_b,
                SUM(p.price * li.quantity) AS total_price
            FROM orders o
            JOIN line_items li ON o.order_id = li.order_id
            JOIN products p ON li.product_id = p.product_id
            GROUP BY o.order_id
        ) AS order_totals
        ON c.customer_id = order_totals.customer_id_b
        GROUP BY c.customer_id;
    """)
    print_rows(cursor)

    print("\nTASK 3: Creating new order for Perez and Sons")

    cursor.execute("SELECT customer_id FROM customers WHERE customer_name='Perez and Sons';")
    customer_id = cursor.fetchone()[0]

    cursor.execute("SELECT employee_id FROM employees WHERE first_name='Miranda' AND last_name='Harris';")
    employee_id = cursor.fetchone()[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5;")
    product_ids = [row[0] for row in cursor.fetchall()]

    conn.execute("BEGIN")
    cursor.execute("INSERT INTO orders (customer_id, employee_id) VALUES (?, ?) RETURNING order_id;", (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    for pid in product_ids:
        cursor.execute("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, 10);", (order_id, pid))

    conn.commit()

    cursor.execute("""
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ?;
    """, (order_id,))
    print_rows(cursor)


    print("\nTASK 4: Employees with more than 5 orders")
    cursor.execute("""
        SELECT
            e.employee_id,
            e.first_name,
            e.last_name,
            COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(o.order_id) > 5;
    """)
    print_rows(cursor)

    conn.close()

if __name__ == "__main__":
    main()
