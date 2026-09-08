from pathlib import Path
from flask import Flask, abort, request

app = Flask(__name__)
root = Path(__file__).with_name("exports")
exports = {"latest": root / "alice.csv"}


@app.get("/account/exports/download")
def download():
    path = exports.get(request.args.get("id"))
    return path.read_text() if path else abort(404)


app.run(port=5000)
