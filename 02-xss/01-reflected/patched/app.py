from flask import Flask, jsonify, make_response, render_template_string, request

app = Flask(__name__)


@app.get("/login")
def login():
    response = make_response('Logged in. Continue to <a href="/search?q=cookies">search</a>.')
    response.set_cookie("session", "alice", httponly=True)
    return response


@app.get("/api/me")
def me():
    if request.cookies.get("session") != "alice":
        return jsonify(error="login required"), 401
    return jsonify(email="alice@example.test", recovery_hint="private account data")


@app.get("/search")
def search():
    return render_template_string(
        "<!doctype html><h1>Knowledge base</h1><p>Results for {{ query }}</p>",
        query=request.args.get("q", ""),
    )


app.run(port=5000)
