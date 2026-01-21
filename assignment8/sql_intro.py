import os
import sqlite3

DB_PATH = "../db/magazines.db"

def create_connection(db_file):
    """Create a database connection to a SQLite database"""
    os.makedirs(os.path.dirname(db_file), exist_ok=True)

    # Remove old database
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Old database removed: {db_file}")

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
        conn.execute("PRAGMA foreign_keys = 1")  # Enforce foreign keys
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_tables(conn):
    """Create tables in the database"""
    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE publishers (
            name TEXT PRIMARY KEY NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE magazines (
            name TEXT PRIMARY KEY NOT NULL,
            publisher_name TEXT NOT NULL,
            FOREIGN KEY (publisher_name) REFERENCES publishers(name)
        )
        """)
        cursor.execute("""
        CREATE TABLE subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            UNIQUE(name, address)
        )
        """)
        cursor.execute("""
        CREATE TABLE subscriptions (
            subscriber_id INTEGER NOT NULL,
            magazine_name TEXT NOT NULL,
            expiration_date TEXT NOT NULL,
            PRIMARY KEY (subscriber_id, magazine_name),
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
            FOREIGN KEY (magazine_name) REFERENCES magazines(name)
        )
        """)
        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def add_publisher(conn, name):
    try:
        conn.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(conn, name, publisher_name):
    try:
        conn.execute("INSERT INTO magazines (name, publisher_name) VALUES (?, ?)", (name, publisher_name))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Cannot add magazine '{name}': {e}")

def add_subscriber(conn, name, address):
    try:
        conn.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Subscriber '{name}' at '{address}' already exists.")

def add_subscription(conn, subscriber_id, magazine_name, expiration_date):
    try:
        conn.execute(
            "INSERT INTO subscriptions (subscriber_id, magazine_name, expiration_date) VALUES (?, ?, ?)",
            (subscriber_id, magazine_name, expiration_date)
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Cannot add subscription: {e}")

def main():
    conn = create_connection(DB_PATH)
    if not conn:
        return

    create_tables(conn)

    # Add publishers
    add_publisher(conn, "Tech Today")
    add_publisher(conn, "Health Weekly")
    add_publisher(conn, "Fashion Forward")

    # Add magazines
    add_magazine(conn, "AI Monthly", "Tech Today")
    add_magazine(conn, "Wellness Daily", "Health Weekly")
    add_magazine(conn, "Style Star", "Fashion Forward")

    # Add subscribers
    add_subscriber(conn, "Alice Johnson", "123 Main St")
    add_subscriber(conn, "Bob Smith", "456 Oak Ave")
    add_subscriber(conn, "Charlie Brown", "789 Pine Rd")

    # Add subscriptions
    add_subscription(conn, 1, "AI Monthly", "2026-12-31")
    add_subscription(conn, 2, "Wellness Daily", "2026-06-30")
    add_subscription(conn, 3, "Style Star", "2026-09-30")
    add_subscription(conn, 1, "Wellness Daily", "2026-11-30")

    # task 4
    print("\nAll subscribers:")
    for row in conn.execute("SELECT * FROM subscribers"):
        print(row)

    print("\nAll magazines sorted by name:")
    for row in conn.execute("SELECT * FROM magazines ORDER BY name"):
        print(row)

    print("\nMagazines published by 'Health Weekly':")
    query = """
    SELECT magazines.name 
    FROM magazines 
    JOIN publishers ON magazines.publisher_name = publishers.name
    WHERE publishers.name = ?
    """
    for row in conn.execute(query, ("Health Weekly",)):
        print(row)

    conn.close()
    print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()
