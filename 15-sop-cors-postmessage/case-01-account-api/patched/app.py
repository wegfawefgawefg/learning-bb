from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/api/account")
def account():
    response = jsonify(email="alice@example.test")
    if request.headers.get("Origin") == "https://app.example.test":
        response.headers["Access-Control-Allow-Origin"] = "https://app.example.test"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        response.headers["Vary"] = "Origin"
    return response


app.run(port=5000, ssl_context="adhoc")
