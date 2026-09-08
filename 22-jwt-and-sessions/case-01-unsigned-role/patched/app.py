import base64, hashlib, hmac, json
from flask import Flask, jsonify, request

app = Flask(__name__)
key = b"server-only-development-key"


def encode(data):
    body = base64.urlsafe_b64encode(json.dumps(data).encode()).decode().rstrip("=")
    return body + "." + hmac.new(key, body.encode(), hashlib.sha256).hexdigest()


@app.get("/login")
def login():
    return jsonify(token=encode({"sub": "alice", "role": "user"}))


@app.get("/api/admin/audit")
def audit():
    try:
        body, signature = request.headers["Authorization"].removeprefix("Bearer ").split(".")
        expected = hmac.new(key, body.encode(), hashlib.sha256).hexdigest()
    except ValueError:
        return jsonify(error="invalid token"), 401
    if not hmac.compare_digest(signature, expected):
        return jsonify(error="invalid token"), 401
    claims = json.loads(base64.urlsafe_b64decode(body + "=" * (-len(body) % 4)))
    return (
        jsonify(secret="audit")
        if claims.get("role") == "admin"
        else (jsonify(error="forbidden"), 403)
    )


app.run(port=5000)
