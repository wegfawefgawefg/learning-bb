import re, subprocess
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.post("/api/diagnostics/dns")
def dns():
    host = request.get_json()["host"]
    if not re.fullmatch(r"[A-Za-z0-9.-]+", host):
        return jsonify(error="host"), 400
    result = subprocess.run(
        ["printf", "lookup: %s", host], capture_output=True, text=True, timeout=2
    )
    return jsonify(output=result.stdout)


app.run(port=5000)
