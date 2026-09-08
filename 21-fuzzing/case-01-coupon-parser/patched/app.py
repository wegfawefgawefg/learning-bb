import re
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.post("/api/coupons/quote")
def quote():
    match = re.fullmatch(r"([A-Z]{3,12}):(\d{1,2})", request.get_json().get("code", ""))
    if not match:
        return jsonify(error="invalid code"), 400
    value = int(match.group(2))
    if value > 30:
        return jsonify(error="discount limit"), 400
    return jsonify(campaign=match.group(1), discount=value, total=100 - value)


app.run(port=5000)
