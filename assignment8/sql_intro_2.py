import sqlite3
import pandas as pd
import os
os.makedirs("../db", exist_ok=True)
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS line_items;")
cursor.execute("DROP TABLE IF EXISTS products;")
cursor.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL
);
""")
cursor.execute("""
CREATE TABLE line_items (
    line_item_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")
products = [
    (1, "Pen", 1.50),
    (2, "Notebook", 3.00),
    (3, "Pencil", 0.75),
    (4, "Eraser", 0.50),
    (5, "Marker", 2.00)
]

cursor.executemany(
    "INSERT INTO products VALUES (?, ?, ?);",
    products
)
line_items = [
    (1, 1, 10),
    (2, 2, 5),
    (3, 3, 20),
    (4, 1, 15),
    (5, 4, 8),
    (6, 5, 6),
    (7, 2, 7),
    (8, 3, 12)
]

cursor.executemany(
    "INSERT INTO line_items VALUES (?, ?, ?);",
    line_items
)
conn.commit()

query = """
SELECT
    li.line_item_id,
    li.quantity,
    p.product_id,
    p.product_name,
    p.price
FROM line_items li
JOIN products p
    ON li.product_id = p.product_id
"""

df = pd.read_sql_query(query, conn)

print("\nInitial DataFrame:")
print(df.head())
df["total"] = df["quantity"] * df["price"]

print("\nWith total column:")
print(df.head())

summary_df = (
    df.groupby("product_id")
      .agg({
          "line_item_id": "count",
          "total": "sum",
          "product_name": "first"
      })
      .reset_index()
)

summary_df = summary_df.sort_values("product_name")

print("\nSummary DataFrame:")
print(summary_df)
summary_df.to_csv("order_summary.csv", index=False)

conn.close()

print("\n✅ SUCCESS: Database created and order_summary.csv written")
