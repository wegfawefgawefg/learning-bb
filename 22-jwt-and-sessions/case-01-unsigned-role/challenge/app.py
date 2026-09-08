import base64, json
from flask import Flask, jsonify, request

app = Flask(__name__)


def encode(data):
    return base64.urlsafe_b64encode(json.dumps(data).encode()).decode().rstrip("=")


def decode(token):
    return json.loads(base64.urlsafe_b64decode(token + "=" * (-len(token) % 4)))


@app.get("/login")
def login():
    return jsonify(token=encode({"sub": "alice", "role": "user"}))


@app.get("/api/admin/audit")
def audit():
    claims = decode(request.headers["Authorization"].removeprefix("Bearer "))
    return (
        jsonify(secret="FLAG{unsigned_claim_became_authority}")
        if claims.get("role") == "admin"
        else (jsonify(error="forbidden"), 403)
    )


app.run(port=5000)
