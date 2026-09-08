from flask import Flask, request

app = Flask(__name__)
cache = {}


@app.post("/cache/reset")
def reset():
    cache.clear()
    return "cleared"


@app.get("/password/reset")
def page():
    key = request.path
    if key not in cache:
        host = request.headers.get("X-Forwarded-Host", request.host)
        cache[key] = (
            f"<!doctype html><a href='http://{host}/password/continue?token=alice-reset'>Continue reset</a>"
        )
    return cache[key], 200, {"X-Lab-Cache": "HIT" if key in cache else "MISS"}


app.run(port=5000)
