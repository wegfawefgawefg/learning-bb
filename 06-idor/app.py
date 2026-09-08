from flask import Flask, abort, jsonify, request

app = Flask(__name__)
sessions = {
    "alice-session": "alice",
    "bob-session": "bob",
}
notes = {
    1: {"owner": "alice", "body": "mine"},
    2: {"owner": "bob", "body": "FLAG{idor}"},
}


def current_user():
    token = request.headers.get("Authorization", "").removeprefix("Bearer ")
    username = sessions.get(token)
    if username is None:
        abort(401)
    return username


@app.get("/vuln/<int:i>")
def vuln(i):
    current_user()
    return jsonify(notes.get(i, {}))


@app.get("/fixed/<int:i>")
def fixed(i):
    n = notes.get(i)
    return jsonify(n) if n and n["owner"] == current_user() else ("not found", 404)


app.run(port=5000)
