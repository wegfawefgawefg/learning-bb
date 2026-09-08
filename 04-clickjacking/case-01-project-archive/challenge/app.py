from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
PROJECT = {"name": "Quarterly launch", "archived": False}


@app.get("/login")
def login():
    response = make_response('<a href="/projects/launch/settings">Project settings</a>')
    response.set_cookie("session", "owner-session", httponly=True)
    return response


@app.get("/projects/launch/settings")
def settings():
    if request.cookies.get("session") != "owner-session":
        return "login required", 401
    return """<!doctype html><style>button{margin:90px 0 0 90px}</style>
    <form method=post action=/projects/launch/archive><button>Archive project</button></form>"""


@app.post("/projects/launch/archive")
def archive():
    if request.cookies.get("session") != "owner-session":
        return "login required", 401
    PROJECT["archived"] = True
    return jsonify(PROJECT)


@app.get("/api/projects/launch")
def status():
    return jsonify(PROJECT)


app.run(port=5000)
