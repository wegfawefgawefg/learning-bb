import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)
DATABASE = Path(__file__).with_name("shop.db")


@app.get("/api/products/search")
def search():
    term = request.args.get("q", "")
    with sqlite3.connect(DATABASE) as connection:
        rows = connection.execute(
            "SELECT name, description FROM products WHERE name LIKE ?", (f"%{term}%",)
        ).fetchall()
    return jsonify(rows)


app.run(port=5000)
