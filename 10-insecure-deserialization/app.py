import base64, pickle
from flask import Flask, request

app = Flask(__name__)


@app.post("/vuln")
def vuln():
    return repr(pickle.loads(base64.b64decode(request.data)))


@app.post("/fixed")
def fixed():
    v = request.get_json(force=True)
    return (
        v
        if set(v) == {"theme"} and v["theme"] in ("light", "dark")
        else ("bad schema", 400)
    )


app.run(port=5000)
