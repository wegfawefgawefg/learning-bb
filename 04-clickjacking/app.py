from flask import Flask, make_response

app = Flask(__name__)


@app.get("/vuln")
def vuln():
    return """<!doctype html>
    <html lang="en">
    <head><meta charset="utf-8"><title>Project settings</title></head>
    <body><button style="margin: 70px">Delete project</button></body>
    </html>"""


@app.get("/fixed")
def fixed():
    r = make_response(vuln())
    r.headers["Content-Security-Policy"] = "frame-ancestors 'none'"
    r.headers["X-Frame-Options"] = "DENY"
    return r


@app.get("/attack")
def attack():
    return """<!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>Clickjacking demonstration</title>
      <style>
        iframe { opacity: 0.15; }
        .lure { position: absolute; left: 75px; top: 75px; }
      </style>
    </head>
    <body>
      <button class="lure">Claim prize</button>
      <iframe src="/vuln" width="400" height="180" title="Framed target"></iframe>
    </body>
    </html>"""


app.run(port=5000)
