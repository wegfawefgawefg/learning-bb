import secrets
from flask import Flask, redirect, request, session

app = Flask(__name__)
app.secret_key = "dev"
codes = {"alice-code": "alice"}


@app.get("/login")
def login():
    session["oauth_state"] = secrets.token_urlsafe(24)
    return redirect("/oauth/callback?code=alice-code&state=" + session["oauth_state"])


@app.get("/oauth/callback")
def callback():
    expected = session.pop("oauth_state", None)
    if not expected or not secrets.compare_digest(expected, request.args.get("state", "")):
        return "invalid state", 403
    session["user"] = codes.get(request.args.get("code"))
    return "logged in"


app.run(port=5000)
