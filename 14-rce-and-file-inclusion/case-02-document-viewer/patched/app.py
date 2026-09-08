from pathlib import Path
from flask import Flask, abort, request

app = Flask(__name__)
root = Path(__file__).with_name("documents")
allowed = {"welcome": root / "welcome.txt"}


@app.get("/documents/view")
def view():
    path = allowed.get(request.args.get("template"))
    return path.read_text() if path else abort(404)


app.run(port=5000)
