from flask import Flask, jsonify, request

app = Flask(__name__)


@app.post("/api/coupons/quote")
def quote():
    code = request.get_json()["code"]
    campaign, discount = code.split(":")
    value = int(discount)
    if value > 30:
        return jsonify(error="discount limit"), 400
    return jsonify(campaign=campaign, discount=value, total=100 - value)


app.run(port=5000)
