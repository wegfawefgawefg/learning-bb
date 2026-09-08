import subprocess
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.post("/api/diagnostics/dns")
def dns():
    host = request.get_json()["host"]
    result = subprocess.run(
        f"printf 'lookup: '; printf {host}", shell=True, capture_output=True, text=True, timeout=2
    )
    return jsonify(output=result.stdout + result.stderr)


app.run(port=5000)
