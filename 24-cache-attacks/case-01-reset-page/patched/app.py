from flask import Flask

app = Flask(__name__)


@app.get("/password/reset")
def page():
    return (
        "<!doctype html><a href='/password/continue'>Continue reset</a>",
        200,
        {"Cache-Control": "no-store"},
    )


app.run(port=5000)
