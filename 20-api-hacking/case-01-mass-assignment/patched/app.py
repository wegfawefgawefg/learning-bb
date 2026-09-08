from flask import Flask, jsonify, request

app = Flask(__name__)
user = {"display_name": "Alice", "role": "user", "plan": "free"}


@app.get("/api/me")
def me():
    return jsonify(user)


@app.patch("/api/me")
def update():
    data = request.get_json()
    if set(data) - {"display_name"}:
        return jsonify(error="immutable field"), 400
    user.update(data)
    return jsonify(user)


app.run(port=5000)
