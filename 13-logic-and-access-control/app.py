from flask import Flask, jsonify, request

app = Flask(__name__)
prices = {"1": 25}
sessions = {"alice-token": {"role": "user"}}


@app.post("/vuln/buy")
def vb():
    return jsonify(charged=int(request.form["price"]))


@app.post("/fixed/buy")
def fb():
    return jsonify(charged=prices[request.form["item"]])


@app.get("/vuln/admin")
def va():
    return "FLAG{admin}" if request.args.get("role") == "admin" else ("no", 403)


@app.get("/fixed/admin")
def fa():
    return (
        "FLAG{admin}"
        if sessions.get(request.headers.get("Authorization"), {}).get("role") == "admin"
        else ("no", 403)
    )


app.run(port=5000)
