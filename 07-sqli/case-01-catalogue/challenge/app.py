import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)
DATABASE = Path(__file__).with_name("shop.db")


def reset():
    with sqlite3.connect(DATABASE) as connection:
        connection.executescript(
            "DROP TABLE IF EXISTS products; DROP TABLE IF EXISTS staff_notes; CREATE TABLE products(id INTEGER PRIMARY KEY,name TEXT,description TEXT); CREATE TABLE staff_notes(id INTEGER PRIMARY KEY,note TEXT); INSERT INTO products VALUES(1,'Proxy Notebook','Grid paper'),(2,'Packet Mug','Ceramic'),(3,'Recon Cards','Pocket cards'); INSERT INTO staff_notes VALUES(1,'FLAG{union_crosses_table_boundary}');"
        )


@app.get("/api/products/search")
def search():
    term = request.args.get("q", "")
    sql = f"SELECT name, description FROM products WHERE name LIKE '%{term}%'"
    try:
        with sqlite3.connect(DATABASE) as connection:
            return jsonify(connection.execute(sql).fetchall())
    except sqlite3.Error:
        return jsonify(error="search unavailable"), 500


reset()
app.run(port=5000)
