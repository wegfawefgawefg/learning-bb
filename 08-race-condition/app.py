import threading, time
from flask import Flask, jsonify

app = Flask(__name__)
state = {"used": False, "balance": 0}
lock = threading.Lock()


def redeem():
    if state["used"]:
        return jsonify(state), 409
    time.sleep(0.15)
    state["used"] = True
    state["balance"] += 10
    return jsonify(state)


@app.post("/vuln")
def vuln():
    return redeem()


@app.post("/fixed")
def fixed():
    with lock:
        return redeem()


app.run(port=5000, threaded=True)
