import threading
from flask import Flask, jsonify

app = Flask(__name__)
account = {"balance": 0, "promo_used": False}
lock = threading.Lock()


@app.get("/api/account")
def status():
    return jsonify(account)


@app.post("/api/promotions/welcome/redeem")
def redeem():
    with lock:
        if account["promo_used"]:
            return jsonify(error="already redeemed"), 409
        account["balance"] += 10
        account["promo_used"] = True
        return jsonify(account)


app.run(port=5000, threaded=True)
