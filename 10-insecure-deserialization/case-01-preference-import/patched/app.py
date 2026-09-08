from flask import Flask, jsonify, request

app = Flask(__name__)


@app.post("/api/preferences/import")
def load():
    value = request.get_json()
    if set(value) != {"theme"} or value["theme"] not in ("light", "dark"):
        return jsonify(error="schema"), 400
    return jsonify(imported=value)


app.run(port=5000)
