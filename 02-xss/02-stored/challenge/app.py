from flask import Flask, jsonify, redirect, request

app = Flask(__name__)
feedback = []


@app.post("/feedback")
def submit():
    feedback.append(request.form.get("message", ""))
    return redirect("/thanks")


@app.get("/thanks")
def thanks():
    return "<!doctype html><p>Thanks. A moderator will review your message.</p>"


@app.get("/api/moderator/context")
def context():
    return jsonify(queue="priority", internal_note="FLAG{stored_xss_reaches_moderator}")


@app.get("/moderation")
def moderation():
    items = "".join(f"<article>{message}</article>" for message in feedback)
    return f"<!doctype html><h1>Moderation queue</h1>{items}"


app.run(port=5000)
