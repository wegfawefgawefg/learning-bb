from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
codes = {"alice-code": "alice", "attacker-code": "attacker"}


@app.get("/oauth/callback")
def callback():
    user = codes.get(request.args.get("code"))
    response = make_response(jsonify(logged_in_as=user))
    response.set_cookie("session", user or "")
    return response


@app.get("/api/me")
def me():
    return jsonify(user=request.cookies.get("session"))


app.run(port=5000)
