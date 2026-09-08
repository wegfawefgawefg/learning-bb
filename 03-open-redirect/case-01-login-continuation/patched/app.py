from flask import Flask, abort, redirect, render_template_string, request

app = Flask(__name__)
DESTINATIONS = {"projects": "/projects", "profile": "/profile"}


@app.route("/login", methods=["GET", "POST"])
def login():
    destination_key = request.values.get("continue", "projects")
    destination = DESTINATIONS.get(destination_key)
    if destination is None:
        abort(400, "unknown continuation")
    if request.method == "POST":
        return redirect(destination)
    return render_template_string(
        """<!doctype html><h1>Acme sign in</h1>
        <form method=post><input type=hidden name=continue value="{{ key }}">
        <input name=email value=alice@example.test><button>Sign in</button></form>""",
        key=destination_key,
    )


@app.get("/projects")
def projects():
    return "<h1>Your projects</h1>"


@app.get("/profile")
def profile():
    return "<h1>Your profile</h1>"


app.run(port=5000)
