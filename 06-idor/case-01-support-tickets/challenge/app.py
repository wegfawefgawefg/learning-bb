from flask import Flask, abort, jsonify, request

app = Flask(__name__)
SESSIONS = {"alice-token": "alice", "bob-token": "bob"}
TICKETS = {
    "TKT-7F21": {"owner": "alice", "subject": "Cannot change avatar", "body": "PNG rejected"},
    "TKT-91B4": {
        "owner": "bob",
        "subject": "Private billing issue",
        "body": "FLAG{cross_account_ticket}",
    },
}


def actor():
    token = request.headers.get("Authorization", "").removeprefix("Bearer ")
    username = SESSIONS.get(token)
    if not username:
        abort(401)
    return username


@app.get("/api/me")
def me():
    return jsonify(username=actor())


@app.get("/api/tickets")
def tickets():
    username = actor()
    return jsonify(
        [
            {"id": key, "subject": value["subject"]}
            for key, value in TICKETS.items()
            if value["owner"] == username
        ]
    )


@app.get("/api/tickets/<ticket_id>")
def ticket(ticket_id):
    actor()
    item = TICKETS.get(ticket_id)
    return jsonify(item) if item else (jsonify(error="not found"), 404)


app.run(port=5000)
