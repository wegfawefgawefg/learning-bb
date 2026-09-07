from urllib.parse import urlparse
from flask import Flask, abort, redirect, request

app = Flask(__name__)


@app.get("/vuln")
def vuln():
    return redirect(request.args.get("next", "/"))


@app.get("/fixed")
def fixed():
    t = request.args.get("next", "/")
    p = urlparse(t)
    if p.scheme or p.netloc or not t.startswith("/"):
        abort(400)
    return redirect(t)


app.run(port=5000)
