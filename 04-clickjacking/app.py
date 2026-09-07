from flask import Flask, make_response

app = Flask(__name__)


@app.get("/vuln")
def vuln():
    return '<button style="margin:70px">Delete project</button>'


@app.get("/fixed")
def fixed():
    r = make_response(vuln())
    r.headers["Content-Security-Policy"] = "frame-ancestors 'none'"
    r.headers["X-Frame-Options"] = "DENY"
    return r


@app.get("/attack")
def attack():
    return "<style>iframe{opacity:.15}.x{position:absolute;left:75px;top:75px}</style><button class=x>Claim prize</button><iframe src=/vuln width=400 height=180></iframe>"


app.run(port=5000)
