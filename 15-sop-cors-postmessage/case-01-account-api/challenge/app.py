from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


@app.get("/login")
def login():
    response = make_response("logged in")
    response.set_cookie("session", "alice", samesite="None", secure=True)
    return response


@app.get("/api/account")
def account():
    response = jsonify(email="alice@example.test", recovery_code="FLAG{cors_cross_origin_read}")
    response.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin", "*")
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response


app.run(port=5000, ssl_context="adhoc")
