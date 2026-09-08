from flask import Flask, jsonify, request

app = Flask(__name__)
users = {"alice": {"display_name": "Alice", "role": "user", "plan": "free"}}


@app.get("/api/me")
def me():
    return jsonify(users["alice"])


@app.patch("/api/me")
def update():
    users["alice"].update(request.get_json())
    return jsonify(users["alice"])


@app.get("/api/admin/audit")
def audit():
    return (
        jsonify(entries=["FLAG{assigned_role_reaches_admin_action}"])
        if users["alice"]["role"] == "admin"
        else (jsonify(error="forbidden"), 403)
    )


app.run(port=5000)
