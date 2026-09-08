from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
ACCOUNT = {"email": "alice@example.test"}


@app.get("/login")
def login():
    response = make_response('<a href="/settings">Account settings</a>')
    response.set_cookie("session", "alice-session", httponly=True, samesite="Lax")
    return response


@app.get("/settings")
def settings():
    return """<!doctype html><form method=post action=/settings/email>
    <input name=email value=alice@example.test><button>Change email</button></form>"""


@app.post("/settings/email")
def change_email():
    if request.cookies.get("session") != "alice-session":
        return "login required", 401
    ACCOUNT["email"] = request.form.get("email", "")
    return jsonify(ACCOUNT)


@app.get("/api/account")
def account():
    return jsonify(ACCOUNT)


app.run(port=5000)
