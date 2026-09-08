from flask import Flask, make_response, request

app = Flask(__name__)


@app.after_request
def prevent_framing(response):
    response.headers["Content-Security-Policy"] = "frame-ancestors 'none'"
    response.headers["X-Frame-Options"] = "DENY"
    return response


@app.get("/login")
def login():
    response = make_response('<a href="/projects/launch/settings">Project settings</a>')
    response.set_cookie("session", "owner-session", httponly=True)
    return response


@app.get("/projects/launch/settings")
def settings():
    if request.cookies.get("session") != "owner-session":
        return "login required", 401
    return """<!doctype html><form method=post action=/projects/launch/archive>
    <label>Type ARCHIVE <input name=confirmation></label><button>Archive</button></form>"""


@app.post("/projects/launch/archive")
def archive():
    if (
        request.cookies.get("session") != "owner-session"
        or request.form.get("confirmation") != "ARCHIVE"
    ):
        return "confirmation required", 403
    return "project archived"


app.run(port=5000)
