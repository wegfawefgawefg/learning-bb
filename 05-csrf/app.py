from flask import Flask, abort, make_response, request

app = Flask(__name__)


@app.get("/login")
def login():
    r = make_response(
        'Logged in as Alice. Try the <a href="/profile">legitimate form</a>, '
        "then open http://127.0.0.1:5001."
    )
    r.set_cookie("session", "alice", httponly=True, samesite="Lax")
    r.set_cookie("csrf", "token", samesite="Lax")
    return r


@app.get("/profile")
def profile():
    return """<!doctype html>
    <html lang="en"><head><meta charset="utf-8"><title>Profile</title></head>
    <body>
      <form method="post" action="/fixed">
        <input type="hidden" name="csrf" value="token">
        <input name="email" value="alice@example.test">
        <button>Change email legitimately</button>
      </form>
    </body></html>"""


@app.post("/vuln")
def vuln():
    if request.cookies.get("session") != "alice":
        abort(401)
    return "email changed to " + request.form.get("email", "")


@app.post("/fixed")
def fixed():
    if request.cookies.get("session") != "alice":
        abort(401)
    if request.form.get("csrf") != request.cookies.get("csrf"):
        abort(403)
    if request.headers.get("Origin") != "http://127.0.0.1:5000":
        abort(403)
    return vuln()


app.run(port=5000)
