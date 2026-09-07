from flask import Flask, abort, make_response, request

app = Flask(__name__)


@app.get("/login")
def login():
    r = make_response("<a href=/attack>attack</a>")
    r.set_cookie("session", "alice")
    r.set_cookie("csrf", "token")
    return r


@app.post("/vuln")
def vuln():
    return "email changed to " + request.form.get("email", "")


@app.post("/fixed")
def fixed():
    if request.form.get("csrf") != request.cookies.get("csrf"):
        abort(403)
    return vuln()


@app.get("/attack")
def attack():
    return "<form id=f method=post action=/vuln><input name=email value=attacker@test></form><script>f.submit()</script>"


app.run(port=5000)
