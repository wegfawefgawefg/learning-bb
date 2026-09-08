from flask import Flask, redirect, render_template_string, request

app = Flask(__name__)


@app.get("/")
def home():
    return '<h1>Acme Projects</h1><a href="/login?continue=/projects">Sign in</a>'


@app.route("/login", methods=["GET", "POST"])
def login():
    destination = request.values.get("continue", "/projects")
    if request.method == "POST":
        return redirect(destination)
    return render_template_string(
        """<!doctype html><h1>Acme sign in</h1>
        <form method=post><input type=hidden name=continue value="{{ destination }}">
        <input name=email value=alice@example.test><button>Sign in</button></form>""",
        destination=destination,
    )


@app.get("/projects")
def projects():
    return "<h1>Your projects</h1>"


app.run(port=5000)
