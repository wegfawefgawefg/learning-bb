import base64, pickle
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.post("/api/preferences/import")
def load():
    return jsonify(imported=pickle.loads(base64.b64decode(request.get_json()["export"])))


app.run(port=5000)
