from flask import Flask, jsonify, make_response

app = Flask(__name__)
project = {"deleted": False}


@app.get("/vuln")
def vuln():
    return """<!doctype html>
    <html lang="en">
    <head><meta charset="utf-8"><title>Project settings</title></head>
    <body>
      <form method="post" action="/delete">
        <button style="margin: 70px">Delete project</button>
      </form>
    </body>
    </html>"""


@app.post("/delete")
def delete_project():
    project["deleted"] = True
    return """<!doctype html>
    <html lang="en"><head><meta charset="utf-8"><title>Deleted</title></head>
    <body><strong>Project deleted</strong></body></html>"""


@app.post("/reset")
def reset_project():
    project["deleted"] = False
    return jsonify(project)


@app.get("/status")
def project_status():
    return jsonify(project)


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
        .stage { position: relative; width: 400px; height: 180px; }
        .lure {
          position: absolute;
          left: 78px;
          top: 78px;
          z-index: 1;
          pointer-events: none;
        }
        iframe {
          position: absolute;
          inset: 0;
          z-index: 2;
          width: 400px;
          height: 180px;
          border: 1px solid #aaa;
          opacity: 0.01;
        }
      </style>
    </head>
    <body>
      <h1>Attacker page</h1>
      <p>The visible lure is underneath a nearly transparent cross-origin iframe.</p>
      <div class="stage">
        <button class="lure">Claim prize</button>
        <iframe src="http://localhost:5000/vuln" title="Framed target"></iframe>
      </div>
      <p>Lab observer: <strong id="status">project exists</strong></p>
      <form method="post" action="/reset"><button>Reset project</button></form>
      <script>
        setInterval(async () => {
          const state = await fetch("/status").then(response => response.json());
          document.querySelector("#status").textContent = state.deleted
            ? "project was deleted"
            : "project exists";
        }, 300);
      </script>
    </body>
    </html>"""


app.run(port=5000)
