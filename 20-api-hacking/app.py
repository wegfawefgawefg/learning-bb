from flask import Flask, jsonify, request

app = Flask(__name__)
profile = {"name": "alice", "role": "user", "plan": "free"}


@app.patch("/vuln")
def vuln():
    profile.update(request.get_json())
    return jsonify(profile)


@app.patch("/fixed")
def fixed():
    d = request.get_json()
    if set(d) - {"name"}:
        return {"error": "immutable"}, 400
    profile.update(d)
    return jsonify(profile)


app.run(port=5000)
