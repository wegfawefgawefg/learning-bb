import secrets

from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.secret_key = "local-development-key"
ACCOUNT = {"email": "alice@example.test"}


@app.get("/login")
def login():
    session["user"] = "alice"
    session["csrf"] = secrets.token_urlsafe(24)
    return f"""<!doctype html><form method=post action=/settings/email>
    <input type=hidden name=csrf value="{session["csrf"]}"><input name=email value=alice@example.test>
    <button>Change email</button></form>"""


@app.post("/settings/email")
def change_email():
    if session.get("user") != "alice":
        return "login required", 401
    if not secrets.compare_digest(request.form.get("csrf", ""), session.get("csrf", "missing")):
        return "invalid CSRF token", 403
    if request.headers.get("Origin") != "http://127.0.0.1:5000":
        return "invalid origin", 403
    ACCOUNT["email"] = request.form.get("email", "")
    return jsonify(ACCOUNT)


app.run(port=5000)
