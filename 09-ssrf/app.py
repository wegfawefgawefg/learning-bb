from urllib.parse import urlparse
import requests
from flask import Flask, abort, request

app = Flask(__name__)


@app.get("/internal")
def internal():
    return "FLAG{internal_service}"


@app.get("/vuln")
def vuln():
    u = request.args.get("url", "")
    p = urlparse(u)
    if p.hostname not in ("127.0.0.1", "localhost"):
        abort(400)
    return requests.get(u, timeout=2).text


@app.get("/fixed")
def fixed():
    return (
        "known upstream"
        if request.args.get("source") == "news"
        else ("bad source", 400)
    )


app.run(port=5000, threaded=True)
