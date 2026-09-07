import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


def db():
    d = sqlite3.connect(":memory:")
    d.executescript(
        "CREATE TABLE users(name,secret);INSERT INTO users VALUES('alice','x'),('admin','FLAG{sqli}');"
    )
    return d


@app.get("/vuln")
def vuln():
    q = "SELECT * FROM users WHERE name='" + request.args.get("name", "") + "'"
    try:
        return jsonify(db().execute(q).fetchall())
    except sqlite3.Error as e:
        return {"error": str(e), "query": q}, 400


@app.get("/fixed")
def fixed():
    return jsonify(
        db()
        .execute("SELECT * FROM users WHERE name=?", (request.args.get("name", ""),))
        .fetchall()
    )


app.run(port=5000)
