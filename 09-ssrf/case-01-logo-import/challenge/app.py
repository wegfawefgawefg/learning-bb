from urllib.parse import urlparse
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/assets/logo")
def logo():
    return "ACME-LOGO"


@app.get("/internal/diagnostics")
def internal():
    return jsonify(deployment_token="FLAG{internal_network_boundary}")


@app.post("/api/invoices/logo/import")
def fetch():
    url = request.get_json()["url"]
    if urlparse(url).scheme not in ("http", "https"):
        return jsonify(error="scheme"), 400
    response = requests.get(url, timeout=2)
    return jsonify(status=response.status_code, preview=response.text[:300])


app.run(port=5000, threaded=True)
